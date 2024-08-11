# Transfer Funds: Users should be able to transfer funds from one account to another.
# Source Account: The account from which the funds will be withdrawn.
# Destination Account: The account to which the funds will be deposited.
# Amount: The amount to be transferred.
# Validation: Ensure that the source account has sufficient funds for the transfer.
# Atomicity: The transfer should be atomic. If the transfer fails, the state should revert to its original state.
# Consistency: The total balance in the system should be consistent before and after the transfer.
# Concurrency: Handle concurrent transfers safely.

import unittest
from app.account import Account
from app.money_transfer import MoneyTransferService

class TestMoneyTransferService(unittest.TestCase):
    
    
    def setUp(self):
        self.account1 = Account()
        self.account1.create_account("Joohn Wick")
        self.account2 = Account()
        self.account2.create_account("Tony Kroos")
    
    def test_transfer_from_one_account_another(self):
        service = MoneyTransferService()
        self.account1.deposit(200)
        service.transfer(self.account1, self.account2, 100)
        self.assertEqual(self.account1.balance, 100, "Money Transfer Failed")
        self.assertEqual(self.account2.balance, 100, "Money Transfer Failed")
        
    def test_transfer_from_one_invalid_account(self):
        service = MoneyTransferService()
        result = service.transfer("DUMMY", self.account2, 100)
        self.assertEqual(result, "Not Valid Accounts", "Accounts Validation Type check Failed")
        
    def test_transfer_from_one_invalid_amount(self):
        service = MoneyTransferService()
        result = service.transfer(self.account1, self.account2, -100)
        self.assertEqual(result, "Not Valid Amount", "Amount check Failed")
        
    def test_transfer_more_one_invalid_amount(self):
        service = MoneyTransferService()
        result = service.transfer(self.account1, self.account2, 1000)
        self.assertEqual(result, "Not Valid Amount", "Amount check Failed")
