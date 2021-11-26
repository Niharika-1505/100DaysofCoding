# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

try:  # Identifies the lines that might be prone to exception
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["Apple"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello")
except KeyError as error_message:  # Except block catches exceptions
    print(f"The Key {error_message} does not exist")
else: # This will be executed only if there are no errors
    content = file.read()
    print(content)
finally:
    print("Finally block is executed no matter what")


# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ['Apple', 'Banana', 'Cherry']
# print(fruit_list[3])

# TypeError
# text = "abc"
# print(text + 5)
