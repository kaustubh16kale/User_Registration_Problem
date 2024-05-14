import unittest
import User_Registration
import os

class TestUserRegistration(unittest.TestCase):
    def test_first_name(self):
        test_file_path=os.path.join(os.path.dirname(__file__),'Test_Cases/test_first_name.txt')
        with open(test_file_path, 'r') as file:
            for name in file:
                first_name = name
                result = User_Registration.valid_first_name(first_name)
                self.assertEqual(result, True, f"first_name {first_name} is not valid")
    
    def test_valid_last_name(self):
        test_file_path=os.path.join(os.path.dirname(__file__),'Test_Cases/test_last_name.txt')
        with open(test_file_path,'r')as file:
            for name in file:
                last_name=name
                result=User_Registration.valid_last_name(last_name)
                self.assertEqual(result,True,f"last_name {last_name} is not valid")
                
    def test_valid_mobile_number_from_file(self):
        test_file_path = os.path.join(os.path.dirname(__file__), 'Test_Cases/test_case_mob_num.txt')
        with open(test_file_path, 'r') as file:
            for number in file:
                mobile_number = number
                result = User_Registration.valid_mobile_number(mobile_number)
                self.assertEqual(result, True, f"Mobile number {mobile_number} is not valid")
    
    def test_mail(self):
        test_file_path=os.path.join(os.path.dirname(__file__),'Test_Cases/test_valid_mail.txt')
        with open(test_file_path, 'r') as file:
            for mail in file:
                mail = mail
                result = User_Registration.valid_mail(mail)
                self.assertEqual(result, True, f"mail {mail} is not valid")


if __name__ == "__main__":
    unittest.main()
