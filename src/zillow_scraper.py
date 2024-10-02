import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Make a request to the Zillow search results page
url = "https://www.zillow.com/homes/your_search_query_rb/"  # Replace with your search query
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Extract data
house_prices = []
for listing in soup.find_all("div", class_="list-card-info"):  # Adjust the tag and class as needed
    price = listing.find("div", class_="list-card-price").text.strip()
    house_prices.append(price)

# Step 4: Save the data to a CSV file
df = pd.DataFrame(house_prices, columns=["House Price"])
df.to_csv("house_prices.csv", index=False)

print("Data saved to house_prices.csv")
print(soup.prettify())  # See the full HTML being parsed
