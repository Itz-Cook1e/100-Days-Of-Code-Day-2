# Super small application (I was super busy today)

# Create list of words for sentence
sentence = ["Unfortunatly", "I", "could", "not", "code", "for", "very", "long", "today,", "so", "I", "am", "making", "this", "extremely", "easy", "program."]

# Print all words on a new line by looping through list with a for loop
for words in sentence:
    print(words)

# Say I am NOT sorry to yall
sorry = ["I", "am", "not", "sorry", "for", "the", "basic", "application."]
# Define word I want to remove from list
not_sorry = ["not"]
# Remove word from list
new_sorry = [words for words in sorry if words not in not_sorry]
# Make new list without said word and join them together (no brackets, commas, and postrophes)
new_new_sorry = " ".join(new_sorry)

# Format (to look decent)
print("\n")
# Print "list" without the word we dont want
print(new_new_sorry)
