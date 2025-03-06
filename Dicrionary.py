import hashlib
import random
import string




letters = string.ascii_letters # -> abcdfghijklmopqrz
numbs = string.digits # -> 0123456789
punc = string.punctuation # -> !@#$%^&*()



let_punc = letters + punc
numbs_punc = numbs + punc
let_nums =  numbs + letters
all_characters = letters + punc + numbs




hash = str(input("Enter Your HASH: "))



type_of_attack = int(input("What type of attack do you want to do? \n\n"
                           "1.) Dictionary Attack\n"
                           "2.) Brute Force Attack \n\n"
                           "Enter Your Choice: "))



dic_list=[]


if type_of_attack == 1:
    print("\n Cracking....")
    dictionary_file = open("rockyou.txt", errors="ignore")
    contents = dictionary_file.readlines()
    for word in contents:
        new_word = word.replace("\n", "")
        dic_list.append(new_word)
    for i in dic_list: 
        if len(hash) == 32:
            dic_hash = hashlib.md5(i.encode("utf-8")).hexdigest()
        elif len(hash) == 40:
            dic_hash = hashlib.sha1(i.encode("utf-8")).hexdigest()
        elif len(hash) == 64:
            dic_hash = hashlib.sha256(i.encode("utf-8")).hexdigest()
            
            
            
        if dic_hash == hash:
            print("\nPassword Found! ", i)
            break
        if dic_hash != hash and dic_list.index(i) == len(dic_list) - 1:
            print("Password not found")
            
            
if type_of_attack == 2:
    type_of_characters = int(input("\nWhat type of characters do you want to do?\n\n"
                                   "1.) All characters\n"
                                   "2.) Only letters\n"
                                   "3.) Letters and Numbers\n"
                                   "4.) Letters and Punctuation\n"
                                   "5.) Numbers and Punctuation\n"
                                   "Enter Your Choice here: "))
    
    if type_of_characters == 1:
        choice_of_char = all_characters
    elif type_of_characters == 2:
        choice_of_char = letters
    elif type_of_characters == 3:
        choice_of_char = let_nums
    elif type_of_characters == 4:
        choice_of_char = let_punc
    elif type_of_characters == 5:
        choice_of_char = numbs_punc
        
        
        
    generated_hash = 0
    gen_str = 0
        
        
        
        
    num_of_char = int(input("\nHow many characters do you want to try?: "))
    print("\nCracking...\n")


    while hash != generated_hash:
        first = random.choice(choice_of_char)
        second = random.choice(choice_of_char)
        third = random.choice(choice_of_char)
     
    
        if num_of_char == 1:
             gen_str = first
        elif num_of_char == 2:
             gen_str = first+second
        elif num_of_char == 3:
             gen_str = first+second+third
       
        
        print(gen_str)
    
    
    
        if len(hash) == 32:
            generated_hash = hashlib.md5(gen_str.encode("utf-8")).hexdigest()
        elif len(hash) == 40:
            generated_hash = hashlib.sha1(gen_str.encode("utf-8")).hexdigest()
        elif len(hash) == 64:
            generated_hash = hashlib.sha256(gen_str.encode("utf-8"))  
        
        
        if hash == generated_hash:
            print(f"Password found! {gen_str}")
            break 
        
        
        
        
        
        
        
    
    
            
            
            
            
            
            
            
            
            

    
            
            
        
        

            
        
            
            
            



