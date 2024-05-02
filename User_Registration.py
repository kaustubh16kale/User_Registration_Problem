import logging
import re

logging.basicConfig(format='%(asctime)s %(message)s', filename="User_Register.log", level=logging.INFO)

def valid_first_name(first_name):
    '''
        Description: function to check the name input is valid or not
        parameter: first_name : name entered by the user
        Return: True if the regex pattern match , False if the pattern does not match
         '''
    if re.match(r'^[A-Z][a-z]{2,}$', first_name):
        return True
    else:
        return False

def valid_last_name(last_name):
    '''
    Description: function to check the last_name 
    Parameter: last_name : last name entered by user
    Return: True if the pattern matches , False if the pattern does not match
    '''
    if re.match(r'[A-Z][a-z]{2,}$',last_name):
        return True
    else:
        return False

def valid_mail(mail):
    '''
    Description: function valid_email used to check if the email is valid or not
    Parameter: mail : email id entered from the user
    Return : True if the mail id followed the pattern , False if the mail id does not match the pattern
    '''
    if re.match(r'^\w+\.?\w+?@\w+\.\w{2,}$',mail):
        return True
    else:
        return False

def valid_mobile_number(mob_num):
    '''
    Description: function to check valid mobile number
    Parameter: mob_num : input taken throug user
    Return: True if the pattern matches else False if it does not match    
    '''
    if re.match(r'^\d{2,} \d{10}',mob_num):
        return True
    else:
        return False

def main():
    ''' main function:
        Return None
    '''
    try:
        first_name = input("Enter the first name: ")
        if valid_first_name(first_name):
            logging.info(f'Valid first name: {first_name}')
            print("Valid first name")
        else:
            logging.warning(f'Invalid first name: {first_name}')
            print("Invalid first name")
        last_name=input("Enter last_name: ")
        if valid_last_name(last_name):
            logging.info(f"Valid Last name: {last_name}")
            print("Valid last name")
        else:
            logging.warning(f"Invalid last name: {last_name}")
            print("Invalid last name")
        mail=input("Enter the mail id: ")
        if valid_mail(mail):
            logging.info(f"Valid mail id: {mail}")
            print("Valid mail id")
        else:
            logging.warning(f"Enter valid mail id: {mail}")
            print("Invalid mail id")
        mob_num=input("Enter the mobile number: ")
        if valid_mobile_number(mob_num):
            logging.info(f"Valid mobile number: {mob_num}")
            print("Valid mobile number")
        else:
            logging.warning(f"Enter valid mobile number: {mob_num}")
            print("Invalid mobile number")
    except Exception as e:
        logging.log(e)


if __name__ == "__main__":
    main()
