import logging
import re

logging.basicConfig(format='%(asctime)s %(message)s', filename="User_Register.log", level=logging.INFO)

def valid_first_name(first_name):
    '''valid_first_name : function to check the name input is valid or not
        first_name : name entered by the user
         return : True if the regex pattern match
         return : False if the pattern does not match'''
    if re.match(r'^[A-Z].{2,}$', first_name):
        return True
    else:
        return False

def main():
    '''main function:
        return None'''
    try:
        first_name = input("Enter the first name: ")
        if valid_first_name(first_name):
            logging.info(f'Valid first name: {first_name}')
            print("Valid first name")
        else:
            logging.warning(f'Invalid first name: {first_name}')
            print("Invalid first name")
    except Exception as e:
        logging.log(e)


if __name__ == "__main__":
    main()
