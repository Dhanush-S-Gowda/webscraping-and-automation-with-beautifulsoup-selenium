from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

WEBSITE_LINK = 'https://appbrewery.github.io/Zillow-Clone/'
FORM_LINK = 'Enter your google form link'

#Extracting data from the website using BeautifulSop 
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    'Accept-Language': "en-US,en;q=0.9"
}

responce = requests.get(WEBSITE_LINK , headers = headers)
soup = BeautifulSoup(responce.text, 'html.parser')

address_elem = soup.findAll(name='address')
address_list = [address.text.strip() for address in address_elem]
print(len(address_list))

price_elem = soup.findAll(name='span', class_='PropertyCardWrapper__StyledPriceLine')
price_list = [price.text.strip() for price in price_elem]
print(len(price_list))

link_elem = soup.find_all(name='a', class_='property-card-link')
link_list = [link['href'] for link in link_elem]
print(len(link_list))


#Filling the form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)
time.sleep(5)

for i in range(len(address_list)):
    add_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    add_area.send_keys(address_list[i])
    price_area.send_keys(price_list[i])
    link_area.send_keys(link_list[i])
    
    submit_button.click()
    time.sleep(2)
    submit_again = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_again.click()
    time.sleep(2)