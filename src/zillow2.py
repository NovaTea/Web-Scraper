import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Use headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Step 1: Make a request to Zillow using Selenium (since it likely loads content dynamically)
url = "https://www.zillow.com/homes/your_search_query_rb/"  # Replace with your search query

# Set up Selenium with ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Optional: wait for the page to fully load
driver.implicitly_wait(10)  # wait for 10 seconds for elements to load

# Step 2: Parse the HTML content after rendering with Selenium
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract data
house_prices = []
for listing in soup.find_all("div", class_="list-card-info"):  # Adjust the tag and class as needed
    price = listing.find("div", class_="list-card-price")
    if price:  # Check if the price element exists to avoid errors
        house_prices.append(price.text.strip())

# Close the Selenium driver
driver.quit()

# Step 4: Save the data to a CSV file
df = pd.DataFrame(house_prices, columns=["House Price"])
df.to_csv("house_prices.csv", index=False)

print("Data saved to house_prices.csv")

# Optional: Print the parsed HTML to verify what you are scraping
print(soup.prettify())
