import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Make a request to the website
url = "https://example.com/jobs"  # Use the actual URL you want to scrape
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Extract data
job_titles = []
for job in soup.find_all("h2", class_="job-title"):  # Adjust the tag and class as needed
    job_titles.append(job.text.strip())

# Step 4: Save the data to a CSV file
df = pd.DataFrame(job_titles, columns=["Job Title"])
df.to_csv("job_listings.csv", index=False)

print("Data saved to job_listings.csv")
