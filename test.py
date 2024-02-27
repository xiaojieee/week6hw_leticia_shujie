class Account:
    numCreated = 0

    def __init__(self, initial_amount, firstname, lastname, pin, account_type):
        self._balance = initial_amount
        self.first_name = firstname
        self.__last_name = lastname
        self.__pin = pin
        self.__account_type = account_type

        Account.numCreated += 1

    def deposit(self, amount, pin):
        if amount >= 0 and pin == self.__pin:
            self._balance += amount

    def withdraw(self, amount, pin):
        if amount >= 0 and pin == self.__pin:
            self._balance -= amount

    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.__last_name

    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    def __str__(self, pin):
        if pin == self.__pin:
            return (f"Account\nFirst Name: {self.get_firstname()}\nLast Name: {self.get_lastname()}"
                    f"\nBalance: ${self.get_balance(pin)}\nAccount Type: {self.__account_type.get_account_type()}"
                    f"\n--------------------------")
        else:
            return "You have no attempts left, please try again later."

    def set_new_pin(self, new_pin):
        self.__pin = new_pin


class AccountType:
    account_types = ['Current', 'Savings', 'ISA']

    def __init__(self, types):
        self.types = types

    def get_account_type(self):
        return self.types


# Create an instance of AccountType
account_type = AccountType('Current')

# Create an instance of Account
lisa_account = Account(100, 'Lisa', 'Simpson', 1234, account_type)

# Print the account details
print(lisa_account.__str__(1234))
