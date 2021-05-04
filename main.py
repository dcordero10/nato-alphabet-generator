student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_dict)

#Loop through rows of a data frame
for (index, row) in nato_dict.iterrows():
    pass
    # print(row.letter)
    #Access index and row
    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dictionary = {row.letter:row.code for (index, row) in nato_dict.iterrows()}
print(nato_dictionary)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    code_word = input("What do you wanna encode?").upper()
    try:
        nato_code = [nato_dictionary[letter] for letter in code_word]
    except KeyError:
        print("There's an issue")
        generate_phonetic()
    else:
        print(nato_code)

generate_phonetic()

