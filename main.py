import json

if __name__ == "__main__":
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
        # total_price = 0
        # for item in products:
        #     price = item['price'].replace(" ", "").replace(" ", "")
        #     item[price] = price
        #     total_price += int(price)
        #
        # print(total_price)

        # new_list_product = []
        # for item in products:
        #     # print(item['colors'])
        #     for color in item['colors']:
        #         if color.lower() == "чорний":
        #             new_list_product.append(item)
        #
        # print(new_list_product)

        # new_list_product = []
        # for item in products:
        #     if "Чорний" in item['colors']:
        #         new_list_product.append(item)
        #
        # print(new_list_product)

        # some_arr = [1, 2, 2, 3]
        # unique_val = []
        #
        # for el in some_arr:
        #     if el not in unique_val:
        #         unique_val.append(el)
        #     continue
        #
        # print(unique_val)

        # for item in products:
        #     for feature in item['features']:
        #         if feature['value'] == "А++":
        #             print(item["title"], feature)

        for item in products:
            with open(f"single_product/{item['id']}.json", "w", encoding="cp1251") as file:
                json.dump(item, file)

        # id = 13
        # with open(f"single_product/{id}.json", "r") as file:
        #     product = json.load(file)
        #     print(product)

        prices = []

        for item in products:
            product_price = int(item['price'].replace(" ", "").replace(" ", ""))
            prices.append(product_price)

        print(prices)

        abs_price = sorted(prices)
        print(abs_price)
        desc_price = sorted(prices, reverse=True)
        print(desc_price)

        for i in range(5):
            print(desc_price[i])
