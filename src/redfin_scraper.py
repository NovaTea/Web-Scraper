import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Use Selenium to load the Redfin search results page
url = "https://www.redfin.com/city/30749/CA/San-Francisco"  # Replace with your search query
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Step 2: Wait for the listings to load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "HomeCardContainer"))  # Adjust this based on Redfin's structure
    )
except Exception as e:
    print("Error: Page took too long to load or elements not found", e)
    driver.quit()

# Step 3: Parse the page content with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Step 4: Extract data (adjust tags/classes based on Redfin's HTML structure)
house_prices = []
for listing in soup.find_all("div", class_="statsValue"):  # Adjust the class as needed
    price = listing.find("span", class_="statsValue")  # Check Redfin's current HTML structure for the price element
    if price:
        house_prices.append(price.text.strip())

# Close the Selenium driver
driver.quit()

# Step 5: Save the data to a CSV file
df = pd.DataFrame(house_prices, columns=["House Price"])
df.to_csv("redfin_house_prices.csv", index=False)

print("Data saved to redfin_house_prices.csv")
