# Account Management

# Account Creation: Users should be able to create a new bank account with a unique account number.
# Account Information: Each account should have basic information, including account number, account holder's name, and balance.


import unittest

from app.account import Account

class TestAccount(unittest.TestCase):
    
    def test_single_account_creation(self):
        account = Account()
        account.create_account("John Whick")
        self.assertTrue(account.account_number is not None, "Account Number is not getting created for new user")
        
    def test_unique_account_number_creation(self):
        account1 = Account()
        account2 = Account()
        account1.create_account("John Whick")
        account2.create_account("Bruce Wayne")
        self.assertTrue(account1.account_number != account2.account_number, "Account Number unique failed")
        
    def test_empty_account_creation(self):
        account = Account()
        with self.assertRaises(ValueError) as context:
         account.create_account(name="")
        
        self.assertEqual(str(context.exception), "Name cannot be empty", "Name Empty Check Failed!")
       
    def test_account_number_retrival(self):
        account = Account()
        account.create_account("Bruce Wayne")
        self.assertTrue(account.check_balance(account.account_number) == 0, "Balance Check By account Number Failed!")
        
    def test_empty_account_number_retrival(self):
        account = Account()
        account.create_account("Bruce Wayne")
        with self.assertRaises(ValueError) as context:
         account.check_balance(account_number=None)
        
        self.assertEqual(str(context.exception), "Account Number cannot be empty", "Account Number Empty Check Failed!")
        
        
    def test_account_number_retrival_with_balance(self):
        account = Account()
        account.create_account("Bruce Wayne")
        account.deposit(100)
        self.assertEqual(account.check_balance(account.account_number), 100, "Balance Check By account Number with balance Failed!")
        
    def test_unique_account_number_balnace_retrieval(self):
        account1 = Account()
        account2 = Account()
        account1.create_account("John Whick")
        account2.create_account("Bruce Wayne")
        account1.deposit(100)
        self.assertEqual(account1.check_balance(account1.account_number), 100, "Balance Check By account Number with balance Failed!")
        self.assertEqual(account2.check_balance(account2.account_number), 0, "Balance Check By account Number with Different Failed!")
        
    def test_multiple_deposit(self):
        account1 = Account()
        account1.create_account("John Whick")
        account1.deposit(100)
        account1.deposit(100)
        self.assertEqual(account1.check_balance(account1.account_number), 200, "Multiple Deposit Failed")
        
        
    def test_retrive_account_deatils_suing_account_nuumber(self):
        account1 = Account()
        account1.create_account("John Whick")
        account1.deposit(100)
        response = account1.retrieve_account_details(account1.account_number)
        result_expected = {"name":"John Whick","balance":100}
        self.assertEqual(response, result_expected, "Retrive Account Info Failed")
        

        
