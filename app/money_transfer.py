


from app.account import Account
import threading

class MoneyTransferService:
    def __init__(self):
        self.valid_transfer = False
        self.failure_message = None
        self.lock = threading.Lock()
    
    def transfer(self, from_account, to_account,amount):
        with self.lock:
            if not self.check_valid_transaction(from_account, to_account, amount):
                return self.failure_message
            try:
                from_account.balance = from_account.balance-amount
                to_account.balance = to_account.balance +amount
            except Exception as e:
                self.handle_failure(from_account, to_account,amount)
            return "Transaction Successfull"
        
                
    def check_valid_transaction(self, from_account, to_account, amount):
        if not isinstance(from_account, Account) or not isinstance(to_account, Account):
            self.failure_message="Not Valid Accounts"
            return False
        if amount <0 or amount > from_account.balance:
            self.failure_message="Not Valid Amount"
            return False
        return True

                