#----------------------------------
#  Strong Password Generator App
#----------------------------------
import string
import random

def generate_password(chars_length:int) -> str:
    
    """
        Generate a strong password based on character percentages:
        - 30% uppercase
        - 30% lowercase
        - 20% digits
        - 20% special characters
    """
    if chars_length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    upper_case = list(string.ascii_uppercase)
    lower_case = list(string.ascii_lowercase)
    digits     = list(string.digits)
    special_chars = list(string.punctuation)


    random.shuffle(upper_case)            
    random.shuffle(lower_case)            
    random.shuffle(digits)            
    random.shuffle(special_chars)            


    part_upper = round(chars_length * (30/100))
    part_lower = round(chars_length * (30/100))
    part_digits = round(chars_length * (20/100))
    part_special = chars_length - (part_upper + part_lower + part_digits)


    password = []
    
    for i in range(part_upper):
        password.append(upper_case[i])
       
    for i in range(part_lower):
        password.append(lower_case[i])
        
    for i in range(part_digits):    
        password.append(digits[i])
    
    for i in range(part_special):     
        password.append(special_chars[i])
        
        
    random.shuffle(password)
    
    return "".join(password)    
    

def main():
    
    
    while True:
           
        user_input = input("How many characters do you need for your password (minimum 8) ? : ")
    
        try:
           chars_length = int(user_input)
           if chars_length < 8:
                print("Length must be at least 8 characters.")
                continue
                
           password = generate_password(chars_length)
           print("\nYour Strong Password is: ", password ,"\n")
           break

        except ValueError:
            print("Please Enter Numbers only.")



if __name__ == "__main__":
    main()