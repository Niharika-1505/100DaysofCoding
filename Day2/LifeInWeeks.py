# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests
remaining_age = 90 - int(age)
days = remaining_age*365
weeks = remaining_age*52
months = remaining_age*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
