import requests
import json

baseURL = "https://fakestoreapi.com"
if __name__ == "__main__":
    ## GET PRODUCTS
    response = requests.get(f"{baseURL}/products")
    data = response.json()
    print(data)

    ## SET PRODUCT
    new_product = {'title': 'test product',
                   'price': 13.5,
                   'description': 'lorem ipsum set',
                   'image': 'https://i.pravatar.cc',
                   'category': 'electronic'}
    resp = requests.post(f"{baseURL}/products", data=new_product)

    ## DELETE PRODUCT
    product_id = 5
    resp = requests.delete(f"{baseURL}/products/{product_id}")

    ## UPDATE PRODUCT

    print(resp.text)
