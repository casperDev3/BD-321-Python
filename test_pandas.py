import pandas as pd
import datetime


# data = {
#     'Name': ["John", "Jane", "Jack"],
#     'Age': [25, 26, 11],
#     'City': ["New York", "LA", "New York"]
# }
#
# df = pd.DataFrame(data)


exel_file_path = f"data-{datetime.datetime.now().date()}.xlsx"
# df.to_excel(exel_file_path, index=False)
df = pd.read_excel(exel_file_path)
names = []
age = []
cities = []
for _, row in df.iterrows():
    names.append(row['Name'])
    age.append(row["Age"])
    cities.append(row["City"])

print(names, age, cities)