class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string representation."""
        result = 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """Deposits an amount into the balance."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws an amount from the balance."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __lt__(self, other):
        """Compares accounts by name."""
        return self.name < other.name

    def __eq__(self, other):
        """Checks equality of accounts by name."""
        return self.name == other.name

    def __gt__(self, other):
        """Compares accounts by name."""
        return self.name > other.name
