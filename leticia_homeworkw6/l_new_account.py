import random


# this is our capsule: collection of attributes and methods
#  uses CapWord conventions - classes always have a capitalisation 'Account'
# declaring class Account
class Account:
    # attribute used to keep count of number of account objects created
    numCreated = 0

    # this is a special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used and when create instance of a class
    # change account number, sort code, account type, pin
    # sets the initial attributes of the object
    # initialises the object attributes
    def __init__(self, initial_amount, firstname, lastname, pin):
        self._balance = int(initial_amount)
        self.first_name = firstname.capitalize()
        self.__last_name = str(lastname).capitalize()
        self.__pin = pin  # Assigning the provided PIN directly
        self._account_number = self.generate_account_number()  # Assigning unique account number
        Account.numCreated += 1

    # todo CANT GET TO STORE ACCOUNT NUMBER RANDOM GEN NUMBERS
    def generate_account_number(self):
        # Incrementing the total number of accounts created
        account_number = Account.numCreated + 1
        # Generating a random string of six digits
        # https://blog.finxter.com/python-how-to-generate-a-random-number-with-a-specific-amount-of-digits/
        # stringifies random integers from 0 - - to use string join function to get one string in 6 digits
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
        # Combining the account number and random digits
        return f"{account_number}{random_digits}"

    # Method to deposit money into the account
    def deposit(self, amount, pin):
        if amount >= 0 and pin == self.__pin:
            self._balance += amount
            return self._balance

    # Method to withdraw money from the account
    def withdraw(self, amount, pin):
        if amount >= 0 and pin == self.__pin and self._balance - amount >= 0:
            self._balance -= amount
        else:
            print("Incorrect PIN or negative amount!")

    # Method to get the current balance of the account
    # TODO: GETTERS
    # Methods to set a new last name for the account
    # getters READ and setters WRITE
    # getters RETURN something, setters do not
    # getters can translate or modify the data before returning it
    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance

    def get_firstname(self, pin):
        if pin == self.__pin:
            return self.first_name

    def get_lastname(self):
        return self.__last_name

    # setters: set or write a piece of information
    # setters have parameters
    # setters often validate incoming data
    # setters often contain if statements
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname


    # Method to display account details, including PIN verification
    def input_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input(f"Enter pin for {self.get_firstname(self.__pin)}: ")
            if int(entered_pin) == self.__pin:
                    return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect pin! {attempts} attempts left.")
                else:
                    print("You have no attempts left, please try again later.")
        return False

    # stringification function as object references are not normally printable
    def __str__(self):
        # added num of account objects created from numCreate attribute
        return (f"{'*' * 15} ACCOUNT DETAILS  {'*' * 15}\n"
                f"Account No: {self._account_number}\n"
                f"Name: {self.get_firstname(self.__pin)} {self.get_lastname()}"
                f"\nBalance: ${self.get_balance(self.__pin)}")








# TODO EXTRA:
# create a parent class user: Account_holder - add pin feature but get to be four random numbers
# details of user stored
# TODO: CREATE A CLASS USER  TO STORE DATA (TRY TO CREATE HIEARCHY)
# class User:
#     def __init__(self, firstname, lastname, age, account_type):
#         self.first_name = firstname
#         self.first_name = lastname
#         self.age = age
#         self.account_type = account_type
#
#     # includes function for the user details
#     def show_details(self):
#         print(f"Personal Details\n Name: {self.first_name, self.last_name}\n Age: {self.age}\n "
#                f"Account Type: {self.account_type}")
# TODO CREATE A Randomly generated PIN
# Method to generate a random 4-digit PIN (You can comment this out if you're providing the PIN directly)
# def generate_random_pin(self):
#     return str(random.randint(1000, 9999))
