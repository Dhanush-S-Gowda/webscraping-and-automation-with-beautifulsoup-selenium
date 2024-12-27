# Zillow Clone Data Scraper

This project is a Python script that extracts data from a Zillow clone website and automatically fills a Google Form with the scraped data. It was developed as a capstone project for the "100 Days of Code: The Complete Python Pro Bootcamp" course on Udemy, which can be found [here](https://www.udemy.com/course/100-days-of-code).

## Requirements

To run this project, you'll need:

- Python 3.x
- BeautifulSoup library
- Requests library
- Selenium library
- Chrome WebDriver

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Dhanush-S-Gowda/webscraping-and-automation-with-beautifulsoup-selenium.git
```
2. Install the required Python packages:
```bash
pip install beautifulsoup4 requests selenium
```
3. Download the Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads) and place it in your system's PATH.
4. Modify the `WEBSITE_LINK` and `FORM_LINK` variables in the script with your desired website and Google Form URLs, respectively.
5. Get your `User-Agent` value from (https://myhttpheader.com/) and add it to your header
6. Run the script:
```bash
python scraper.py
```
