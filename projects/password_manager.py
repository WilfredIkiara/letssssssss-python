import random 
import string


def generate_password(min_length, numbers = True ,special_characters = True):
    #the passed variables determine what type of password will be generated
    #it determines the type of characters and their amount
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    #print(special, letters, digits)

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special
      
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char is digits:
            has_number = True
        elif new_char is special:
            has_special = True
        
        meets_criteria = True
        
        if numbers:
            meets_criteria = has_number      
        if special_characters:
            meets_criteria = meets_criteria and has_special
        if len(pwd) == min_length:
            return pwd
    return pwd 

min_length  = int(input("Enter the minimum length of your password"))
has_number  = input("Do you want to have numbers(y/n)").lower()=="y"
has_special  = input("Do you want special characters (y/n)").lower()=="y"
pwd = generate_password(min_length, has_special, has_number)
print(f"your generated password is: {pwd}")