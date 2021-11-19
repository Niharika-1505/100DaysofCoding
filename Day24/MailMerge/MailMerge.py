PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as get_names_from_file:
    names = get_names_from_file.readlines()

with open("./Input/Letters/starting_letter.txt") as get_letter_from_file:
    letter_content = get_letter_from_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_To_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
