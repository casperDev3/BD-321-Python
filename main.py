if __name__ == "__main__":
    # users = [
    #     {
    #         "name": "John",
    #         "age": 31
    #     },
    #     {
    #         "name": "Jane",
    #         "age": 27
    #     },
    #     {
    #         "name": "Jack",
    #         "age": 15
    #     },
    #     {
    #         "name": "John",
    #         "age": 31
    #     }
    # ]
    # temp_age = 6
    # temp_name = users[1]['name']
    # print(temp_age, temp_name)
    print("___ START PROGRAM ___ \n\n")
    system_metrics = input(f"Please choice system metrics:\n"
                           f"c - Celsius\n"
                           f"f - Farengei\n"
                           f"k - Kalvin\n"
                           f"Please choice: ")
    temperature_value = int(input(f"Please input temperatute value:  "))

    # conditional temp
    if system_metrics.lower() == "c":
        print(f"INPUT VALUE: {temperature_value} C\n\n")
        print(f"Kalvin: {round(temperature_value + 273.75, 2)}")
        print(f"Farengeit: {round((temperature_value * (9 / 5)) + 32, 2)}")
    elif system_metrics.lower() == "f":
        print(f"INPUT VALUE: {temperature_value} F\n\n")
        print(f"Kalvin: {((temperature_value - 32) + 273.75) / (9 / 5)}")
        print(f"Celsium: {(temperature_value / (9 / 5)) - 32}")
    else:
        print("CALC SELF!")
