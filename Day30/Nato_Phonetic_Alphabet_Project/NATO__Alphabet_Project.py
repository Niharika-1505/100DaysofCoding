import pandas

# Create a dataframe by reading the csv file
nato_alphabets_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the csv
nato_alphabets_dict = {row.letter: row.code for (index, row) in nato_alphabets_dataframe.iterrows()}
print(nato_alphabets_dict)


# Create a list of dictionary values for all the letters in the name
def generate_phonetic_words():
    name = input("Please enter your Name: ").upper()
    try:
        nato_alphabets = [nato_alphabets_dict[each_letters] for each_letters in name]
    except KeyError:
        print("Please enter only words")
        generate_phonetic_words()
    else:
        print(f"{nato_alphabets}")


generate_phonetic_words()
