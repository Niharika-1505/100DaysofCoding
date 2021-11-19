with open("data.txt", mode="w") as write_to_file:
    write_to_file.write("Hi Neeru..! Welcome to learning files in python.\n")
with open("data.txt") as read_from_file:
    file_contents = read_from_file.read()
    print(f"After writing to the file: {file_contents}")
with open("data.txt", mode="a") as append_to_file:
    append_to_file.write("I am glad you decided to learn")
with open("data.txt") as read_from_file:
    file_contents = read_from_file.read()
    print(f"After appending the file: {file_contents}")
