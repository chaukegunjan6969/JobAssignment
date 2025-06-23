import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.olx.in/items/q-car-cove"

# Send a GET request with headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all listing containers (this may need to be updated based on OLX's HTML structure)
    listings = soup.find_all('li')  # Placeholder, adjust after inspecting OLX HTML

    with open("olx_car_covers.txt", "w", encoding="utf-8") as file:
        for listing in listings:
            title = listing.find('h6')
            price = listing.find('span')

            if title and price:
                file.write(f"Title: {title.get_text(strip=True)}\n")
                file.write(f"Price: {price.get_text(strip=True)}\n")
                file.write("-" * 40 + "\n")
    print("Scraping completed. Results saved in 'olx_car_covers.txt'.")
else:
    print("Failed to fetch page. Status Code:", response.status_code)
