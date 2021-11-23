import pandas

# Create a dataframe by reading the csv file
nato_alphabets_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the csv
nato_alphabets_dict = {row.letter: row.code for (index, row) in nato_alphabets_dataframe.iterrows()}
print(nato_alphabets_dict)

# Create a list of dictionary values for all the letters in the name
name = input("Please enter your Name: ").lower()
nato_alphabets = [nato_alphabets_dict.get(each_letters) for each_letters in name]
print(f"The Nato Alphabets for {name} are {nato_alphabets}")
