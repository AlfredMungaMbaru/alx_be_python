class BankAccount:
    """A class to represent a bank account with basic banking operations."""
    
    def __init__(self, initial_balance=0):
        """Initialize a new bank account with an optional initial balance."""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds exist.
        Returns True if withdrawal is successful, False otherwise.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")