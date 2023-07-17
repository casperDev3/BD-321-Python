import json
import transform_temp as tt

if __name__ == "__main__":
    system_metrics = input(f"Please choice system metrics:\n"
                           f"c - Celsius\n"
                           f"f - Farengei\n"
                           f"k - Kalvin\n"
                           f"Please choice: ")
    temperature_value = int(input(f"Please input temperatute value:  "))

    # conditional temp
    if system_metrics.lower() == "c":
        tt.tranformCelsius(temperature_value)
    elif system_metrics.lower() == "f":
        tt.tranformFarengeit(temperature_value)
    else:
        print("CALC SELF!")
