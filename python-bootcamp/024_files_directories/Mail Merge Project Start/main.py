#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# read file and fine where to insert it
with open("Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()

# read names file
with open("Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as names_file:
    # read each line in the string and append them to a list
    names = names_file.readlines() 
    
    # process the names: remove all whitespaces
    for name in names:
        name = name.strip()
    
    # create the new letter
    for name in names:
        new_letter = letter_contents.replace("[name]", name) 
        with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
    

