from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YLdp6DZKhn5")

print(response)

response.content
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify

print(soup.prettify)
print(response.content)