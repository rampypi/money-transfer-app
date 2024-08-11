
import random

from app.exception import InvalidAmount
import threading

class Account:
    def __init__(self):
        self.account_number = None
        self.name = None
        self.balance = 0
        self.accounts = {}
        self.lock = threading.Lock()
        
    
    def create_account(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.account_number = self.generate_unique_account_number()
        self.name = name
        if self.account_number not in self.accounts:
            self.accounts[self.account_number] = {"name":self.name, "balance":self.balance}
        
        return "Account Created Successfully!"
    
    def generate_unique_account_number(self):
        while True:
            with self.lock:
                unique_number = str(random.randint(10**11, 10**12 - 1))
                if unique_number not in self.accounts:
                    return unique_number
    
    
    def check_balance(self, account_number):
        if account_number and self.account_number in self.accounts:
            return self.accounts[self.account_number]["balance"]
        raise ValueError("Account Number cannot be empty")
    
    def deposit(self, amount):
        if isinstance(amount, int) and amount >0 and self.account_number in self.accounts:
            with self.lock:
                current_balanace = self.accounts[self.account_number]["balance"]
                self.accounts[self.account_number]["balance"] = current_balanace+amount
                self.balance = current_balanace+amount
            return "Succesfully Deposited"
        
        if amount <0:
           raise ValueError("Amount Cannot be less than Zero!")
        raise InvalidAmount("Amount is not valid! Check the Amount again")
    
    
    
    def retrieve_account_details(self, account_number):
        if not account_number and account_number not in self.accounts:
            raise ValueError("Account Number is required! Not in our system kindly check")
        return self.accounts[account_number]
            
