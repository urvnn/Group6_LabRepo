class Bank:
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self, fileName=None):
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank with accounts sorted by name."""
        sorted_accounts = sorted(self.accounts.values())  # Sort accounts by name
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def save(self, fileName=None):
        """Saves pickled accounts to a file."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

