class Permisions():
    
    def __init__(self):
        self.createUser = False
        self.selectUsers = False
        self.selectCustomers = False
        self.selectTransactions = False

    def isCreateUser(self):
        return self.createUser

    def isSelectUsers(self):
        return self.selectUsers

    def isSelectCustomers(self):
        return self.selectCustomers

    def isSelectTransactions(self):
        return self.selectCustomers
    