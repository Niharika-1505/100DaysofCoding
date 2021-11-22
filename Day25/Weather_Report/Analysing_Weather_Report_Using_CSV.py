import csv

with open("weather_data.csv") as report:
    weather_report = csv.reader(report)
    days = []
    temperatures = []
    weather_type = []
    for each_row in weather_report:
        if each_row[0] != 'day' and each_row[1] != 'temp' and each_row[2] != 'condition':
            days.append(each_row[0])
            temperatures.append(int(each_row[1]))
            weather_type.append(each_row[2])
    print(f"Days: {days}\nTemperature: {temperatures}\nWeather: {weather_type}")
