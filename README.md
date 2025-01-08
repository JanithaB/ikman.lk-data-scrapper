
# Ikman.lk site data scraper

This project is a web scraping tool for extracting vehicle details such as model, mileage, and year of manufacture from the Ikman.lk website. The script saves the data into an Excel file for further analysis.

## Features
- Scrapes vehicle information from Ikman.lk
- Stores data in an Excel file
- Runs in headless mode for efficiency

## Prerequisites
- Python 3.7 or higher
- Google Chrome installed
- ChromeDriver compatible with your Chrome version

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/janithab/ikman-scraper.git
   cd ikman-scraper

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt

3. Download ChromeDriver and ensure it's added to your PATH:

- Download ChromeDriver

## Usage

1. Modify the `search_query` variable in the `script.py` file to match your desired search term:
`search_query = "Pulsar 150"`

2. Run the script:
    ```bash
    python script.py

3. The results will be saved in an Excel file named `results.xlsx` in the current directory.

## Notes
The script scrapes the first 10 search results by default.
You can customize the number of results or other details by modifying the `scrape_results` method.

## Troubleshooting
- Ensure the version of ChromeDriver matches your installed version of Google Chrome.
- If the script encounters issues with elements not loading, you can increase the `WebDriverWait timeout value` in the script.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
