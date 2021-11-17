import csv
import pandas as pd

# with open('weather_data.csv') as data_file:
#     # data = data_file.readlines()
#     temp_data = []
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temp_data.append(row[1])
#     print(temp_data)

data = pd.read_csv('weather_data.csv')
# print(data)
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# print(data[data.day == "Monday"])
# print(data[data.temp.max() == data.temp])

# monday = data[data.day == "Monday"]
# monday_temp_in_c = int(monday.temp)
# monday_temp_in_f = (monday_temp_in_c * 9/5) + 32
# print(monday_temp_in_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")