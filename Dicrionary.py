import hashlib  # Module for hashing algorithms (MD5, SHA1, SHA256, etc.)
import random   # Module for generating random choices
import string   # Module for pre-defined character sets (letters, digits, punctuation)

# Pre-defined character sets
letters = string.ascii_letters  # All uppercase and lowercase letters (a-z, A-Z)
numbs = string.digits           # All digits (0-9)
punc = string.punctuation       # All punctuation marks (!@#$%^&*(), etc.)

# Combined character sets for different attack scenarios
let_punc = letters + punc       # Letters + Punctuation
numbs_punc = numbs + punc       # Digits + Punctuation
let_nums = numbs + letters      # Digits + Letters
all_characters = letters + punc + numbs  # All characters combined

# Ask the user to input the hash they want to crack
hash = str(input("Enter Your HASH: "))

# Ask the user to choose the type of attack
type_of_attack = int(input("What type of attack do you want to do? \n\n"
                           "1.) Dictionary Attack\n"
                           "2.) Brute Force Attack \n\n"
                           "Enter Your Choice: "))

# Dictionary Attack
if type_of_attack == 1:
    print("\nCracking....")
    dic_list = []  # List to store words from the dictionary file
    
    # Open the dictionary file (e.g., rockyou.txt)
    dictionary_file = open("rockyou.txt", errors="ignore")
    contents = dictionary_file.readlines()  # Read all lines from the file
    
    # Process each word in the dictionary
    for word in contents:
        new_word = word.replace("\n", "")  # Remove newline characters
        dic_list.append(new_word)  # Add the word to the list
    
    # Iterate through the dictionary list and compare hashes
    for i in dic_list:
        # Determine the hash type based on the length of the input hash
        if len(hash) == 32:
            dic_hash = hashlib.md5(i.encode("utf-8")).hexdigest()  # MD5 hash
        elif len(hash) == 40:
            dic_hash = hashlib.sha1(i.encode("utf-8")).hexdigest()  # SHA1 hash
        elif len(hash) == 64:
            dic_hash = hashlib.sha256(i.encode("utf-8")).hexdigest()  # SHA256 hash
        
        # Compare the generated hash with the input hash
        if dic_hash == hash:
            print("\nPassword Found! ", i)  # Password found
            break
        # If the end of the list is reached and no match is found
        if dic_hash != hash and dic_list.index(i) == len(dic_list) - 1:
            print("Password not found")  # Password not found

# Brute Force Attack
if type_of_attack == 2:
    # Ask the user to choose the type of characters for the brute force attack
    type_of_characters = int(input("\nWhat type of characters do you want to use?\n\n"
                                   "1.) All characters\n"
                                   "2.) Only letters\n"
                                   "3.) Letters and Numbers\n"
                                   "4.) Letters and Punctuation\n"
                                   "5.) Numbers and Punctuation\n"
                                   "Enter Your Choice here: "))
    
    # Set the character pool based on the user's choice
    if type_of_characters == 1:
        choice_of_char = all_characters  # All characters
    elif type_of_characters == 2:
        choice_of_char = letters  # Only letters
    elif type_of_characters == 3:
        choice_of_char = let_nums  # Letters and numbers
    elif type_of_characters == 4:
        choice_of_char = let_punc  # Letters and punctuation
    elif type_of_characters == 5:
        choice_of_char = numbs_punc  # Numbers and punctuation
    
    # Variables to store the generated hash and string
    generated_hash = 0
    gen_str = 0
    
    # Ask the user for the number of characters to try in the brute force attack
    num_of_char = int(input("\nHow many characters do you want to try?: "))
    print("\nCracking...\n")

    # Brute force loop
    while hash != generated_hash:
        # Randomly select characters based on the chosen character pool
        first = random.choice(choice_of_char)
        second = random.choice(choice_of_char)
        third = random.choice(choice_of_char)
        
        # Generate a string based on the number of characters requested
        if num_of_char == 1:
            gen_str = first  # 1-character string
        elif num_of_char == 2:
            gen_str = first + second  # 2-character string
        elif num_of_char == 3:
            gen_str = first + second + third  # 3-character string
        
        # Print the generated string for debugging or progress tracking
        print(gen_str)
        
        # Determine the hash type based on the length of the input hash
        if len(hash) == 32:
            generated_hash = hashlib.md5(gen_str.encode("utf-8")).hexdigest()  # MD5 hash
        elif len(hash) == 40:
            generated_hash = hashlib.sha1(gen_str.encode("utf-8")).hexdigest()  # SHA1 hash
        elif len(hash) == 64:
            generated_hash = hashlib.sha256(gen_str.encode("utf-8")).hexdigest()  # SHA256 hash
        
        # Compare the generated hash with the input hash
        if hash == generated_hash:
            print(f"Password found! {gen_str}")  # Password found
            break
