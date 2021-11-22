import pandas

weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data)
print(type(weather_data))
print(type(weather_data["day"]))

# Get data from columns
print(weather_data["day"])
print(weather_data.day)

# Get data from rows
print(f"Row data: {weather_data[weather_data.day == 'Monday']}")
print(f"Highest Temp in the week:{weather_data[weather_data.temp == weather_data.temp.max()]}")

# Get specific data from a row based on give condition
day_name = weather_data[weather_data.day == 'Tuesday']
print(f"Temperature in °F on Tuesday: {round((day_name.temp * (9 / 5)) + 32)}")

# converting csv data to a dictionary using pandas
data_dict = weather_data.to_dict()
print(f"Weather Data Dictionary: {data_dict}")

# converting a series/column in the csv to a list using pandas
data_list = weather_data["temp"].to_list()
average_temp = round(sum(data_list) / len(data_list))
print(f"Temperatures list: {data_list}\nAverage Temperature is: {average_temp}°C")

# Using mean method from pandas series
average_temperature = round(weather_data["temp"].mean())
print(f"Average Temperature calculated using mean is: {average_temperature}°C")

# Using max method from pandas series
max_temp = weather_data["temp"].max()
print(f"Maximum recorded temperature is: {max_temp}°C")

# Creating a DataFrame from scratch and adding the data to csv
student_data_dict = {
    "students": ["Neeru", "Chandu", "Kowshi", "Nikki", "Kamal"],
    "scores": [98, 95, 89, 88, 92]
}
student_data = pandas.DataFrame(student_data_dict)
student_data.to_csv("student_scores.csv")
