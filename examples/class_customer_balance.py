class Customer:
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name):
        """Return a Customer object whose name is *name* and starting
        balance is 0."""
        self.name = name
        self.balance = 0.0

    def set_balance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

cust=Customer("Shiva")
print "Customer Details:",cust.name,cust.balance
cust.set_balance(23000)
print "Customer Details:",cust.name,cust.balance
cust.withdraw(2000)
print "Customer Details:",cust.name,cust.balance
cust.deposit(5000)
print "Customer Details:",cust.name,cust.balance
cust.withdraw(27000)