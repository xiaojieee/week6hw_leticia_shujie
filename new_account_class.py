
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
    # getter is to get something

    def get_lastname(self):
        return self.__last_name

    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    def __str__(self):
        pin = self.input_pin()
        if pin == self.__pin:
            return (f"Account\nFirst Name: {self.get_firstname()}\nLast Name: {self.get_lastname()}Account type: {self.}"
                    f"\nBalance: ${self.get_balance(pin)}\n--------------------------")
        else:
            return "You have no attempts left, please try again later."

    def input_pin(self):
        attempts = 3
        for i in range(3):
            pin = int(input(f"Enter pin for {self.get_firstname()}: "))
            attempts -= 1
            if pin == self.__pin:
                return pin
            else:
                print(f"Incorrect pin for {self.get_firstname()}, {attempts} attempts left.")
        return None

    def set_new_pin(self, new_pin):
        self.__pin = new_pin


class AccountType:
    account_types = ['Current', 'Savings', 'ISA']

    def __init__(self, types):
        self.types = types

    def get_account_type(self):
        return self.types


if __name__ == "__main__":

    lisa_account = Account(100, 'Lisa', 'Simpson', 1234, 'Current')
    print(lisa_account)

