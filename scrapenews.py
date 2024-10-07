import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://krebsonsecurity.com/"

# Set headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the headlines (contained within h2 tags with class 'entry-title')
    headlines = soup.find_all("h2", class_="entry-title")

    # Print the latest headlines (limit to top 5)
    print("Latest News Headlines from Krebs on Security:")
    for headline in headlines[:5]:
        print("- " + headline.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
