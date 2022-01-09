# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open letter template
with open("./Input/Letters/starting_letter.txt") as content:
    template_letter = content.read()


# open file that include all the names and store in a new list of names
with open("./Input/Names/invited_names.txt") as content:
    names = content.readlines()
    names_list = []
    for name in names:
        new_name = name.strip("\n")
        names_list.append(new_name)

# create letters for every name from the list
for name in names_list:
    print(name)
    new_letter = template_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as content:
        content.write(new_letter)
