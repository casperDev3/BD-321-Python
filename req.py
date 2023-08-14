import requests
import json

baseURL = "https://fakestoreapi.com"
if __name__ == "__main__":
    response = requests.get(f"{baseURL}/products")
    data = response.json()
    for item in data:
        print(f"{item['id']}. {item['title']} -- {item['price']}")