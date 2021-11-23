NATO_ALPHABETS_DICT = {
    "a": "Apple",
    "b": "Banana",
    "c": "Cherry",
    "d": "Dates",
    "e": "Elephant Apple",
    "f": "Fig",
    "g": "Grapes",
    "h": "HoneyDew Melon",
    "i": "Ice Apples",
    "j": "Juniper Berry",
    "k": "kiwi",
    "l": "LoganBerry",
    "m": "Mango",
    "n": "Nectarine",
    "o": "Orange",
    "p": "Pear",
    "q": "Quince",
    "r": "Raspberry",
    "s": "Strawberry",
    "t": "Tangerine",
    "u": "Ugli",
    "v": "Velvet Tamarind",
    "w": "Watermelon",
    "x": "Ximenia",
    "y": "Young Berry",
    "z": "Zhe fruit"
}
name = input("Please enter your Name: ")
# Example for list and dictionary comprehension
Nato_Alphabets = [NATO_ALPHABETS_DICT.get(each_letters) for each_letters in name.lower()]
print(f"1. {Nato_Alphabets}")

range_list = [n * 2 for n in range(1, 6)]
print(f"2. New list created by doubling the values from 1 to 5 :{range_list}")

# Examples for Conditional list comprehension
even_numbers_list = [n for n in range(1, 101) if n % 2 == 0]
print(f"3. Even numbers from 1 to 100 : {even_numbers_list}")
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names_less_letters = [each_name for each_name in names if len(each_name) == 4]
names_with_more_letters = [each_name.upper() for each_name in names if len(each_name) > 4]
print(f"4. Names with 4 letters: {new_names_less_letters}\n5. Names with more than 4 letters: {names_with_more_letters}")

# Squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares = [n ** 2 for n in numbers]
print(f"6. Square root values of [1,1,2,3,5, 8, 13, 21, 34,55] are {squares} respectively")

