def pib(n, s, f):
    pib = s + " " + n[0] + " " + f[0]
    return pib


def calc(num_one, num_two, operator):
    if operator == "+":
        return num_one + num_two
    elif operator == "-":
        return num_one - num_two
    elif operator == "*":
        return num_one * num_two
    elif operator == "/":
        try:
            return num_one / num_two
        except Exception as err:
            return err
    else:
        return "Такий оператор не передбачено!"


if __name__ == "__main__":
    # test = "hello world !"
    # print(test.capitalize())
    # print(test.title())
    # print(test.upper())
    # print(test.lower())
    # print(test.replace("h", "H"))
    #
    # print(test[::-1])
    # print(test.split())
    # print(test.strip())
    #
    # print(len(test.replace(" ", "").replace("!", "")))
    # print(test + " test")

    # # int, float & complex
    # int = 5
    # float = 1.2
    # complex = 12j
    # a = False
    #
    # arr = [1, 3, 5]
    #
    # arr.append('test')
    # # arr.pop()
    # # arr.remove(5)
    # cont = 0
    # for item in arr:
    #     print(item)
    #     cont += 1
    #
    # for i in range(len(arr)):
    #     print(i)
    #     print(arr[i])

    # flag = 0
    # while flag <= 100:
    #     print("test while")
    #     flag += 10
    #     print(flag)
    #
    #     if flag <= 100:
    #         print(flag)
    #         continue
    #     else:
    #         break
    #
    # intials = pib("John", "Doe", "Patrick")
    # print(intials)
    #
    # num_one = int(input("Введіть перше число: "))
    # num_two = int(input("Ведіть друге число: "))
    # operator = input("Оберіть оператор (+, -, *, /): ")
    #
    # result = calc(num_one, num_two, operator)
    #
    # print(result)

    # print(arr)

    numb_arr = []
    start_value = int(input("Start value: "))
    end_value = int(input("End value: ")) + 1
    for i in range(start_value, end_value):
        if i % 3 == 0 and i % 5 == 0:
            numb_arr.append(i)
    print(numb_arr)
