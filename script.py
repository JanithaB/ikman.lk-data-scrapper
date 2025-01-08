from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import openpyxl
import time


class IkmanScraper:
    def __init__(self, search_query, output_file):
        #set to run in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.search_query = search_query
        self.output_file = output_file
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Results"
        self.sheet.append(["Model", "Mileage", "Year of Manufacture"])
    
    #start the scraping process
    def start_scraping(self):
        self.driver.get("http://ikman.lk")
        self.search_item()
        self.scrape_results()
        self.driver.quit()
    
    #search the keyword
    def search_item(self):
        search_box = self.driver.find_element(By.NAME, "query")
        search_box.send_keys(self.search_query)
        search_box.submit()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "list--3NxGO"))
        )
    
    #scrape through search results
    def scrape_results(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, "ul.list--3NxGO li")
        
        for i in range(10):
            results = self.driver.find_elements(By.CSS_SELECTOR, "ul.list--3NxGO li")
            try:
                link = results[i].find_element(By.TAG_NAME, "a")
                href = link.get_attribute("href")

                self.driver.get(href)
                self.scrape_details()
                self.driver.back()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "list--3NxGO"))
                )

            except Exception as e:
                print(f"Error interacting with list item {i}: {e}")
    
    #scrape data from the results
    def scrape_details(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            model_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Model')]/following-sibling::div")
            mileage_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Mileage')]/following-sibling::div")
            YoM_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Year of Manufacture')]/following-sibling::div")

            model = model_element.text
            mileage = mileage_element.text
            year = YoM_element.text

            self.save_to_excel(model, mileage, year)

        except Exception as e:
            print(f"An error occurred while scraping details: {e}")

    #save to the excel file
    def save_to_excel(self, model, mileage, year):
        self.sheet.append([model, mileage, year])
        self.workbook.save(self.output_file)
        print(f"Data saved: {model} | {mileage} | {year}")


if __name__ == "__main__":
    search_query = "Pulsar 150"
    output_file = "results.xlsx"  
    scraper = IkmanScraper(search_query, output_file)
    scraper.start_scraping()
