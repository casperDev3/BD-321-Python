import json
if __name__ == "__main__":
    with open('products.json', "r") as file:
        products = json.load(file)
           

    total_price = 0
    for product in products:
        total_price += product['price']

    print(round(total_price, 2))

