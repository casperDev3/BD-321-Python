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


        some_arr = [1, 2, 2, 3]
        unique_val = []

        for el in some_arr:
            if el not in unique_val:
                unique_val.append(el)
            continue

        print(unique_val)


