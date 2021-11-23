import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(50, 100) for student in names}
print(f"1. Student scores: {student_scores}")
passed_students = {student: score for (student, score) in student_scores.items() if score > 65}
print(f"2. Passed Students: {passed_students}")

# Add length of each word to a dictionary
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_length_dict = {word: len(word) for word in sentence.split()}
print(f"3. Length of each word in a string:{word_length_dict}")

# Converting temperatures in a dictionary from °C to °F
weather_celsius = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_fahrenheit = {day: ((temp_c * 9 / 5) + 32) for (day, temp_c) in weather_celsius.items()}
print(f"4: Temperatures in °F: {weather_fahrenheit}")
