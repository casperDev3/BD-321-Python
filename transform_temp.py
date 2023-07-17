def tranformCelsius(temperature_value):
    print(f"INPUT VALUE: {temperature_value} C\n\n")
    print(f"Kalvin: {round(temperature_value + 273.75, 2)}")
    print(f"Farengeit: {round((temperature_value * (9 / 5)) + 32, 2)}")


def tranformFarengeit(temperature_value):
    print(f"INPUT VALUE: {temperature_value} F\n\n")
    print(f"Kalvin: {((temperature_value - 32) + 273.75) / (9 / 5)}")
    print(f"Celsium: {(temperature_value / (9 / 5)) - 32}")
