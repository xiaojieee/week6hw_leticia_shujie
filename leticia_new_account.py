# this is our capsule
# it is a collection of attributes and methods
# classes always have a capitalisation 'Account'
from random import randint
import secrets

help(super)


# create a parent class user: Account_holder - add pin feature but get to be four random numbers
# details of user stored
# TODO: CREATE A CLASS USER TO STORE DATA
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


# TODO ACCOUNT CLASS: ADD RANDOM 4 DIGITS AS PIN
class Account:
    numCreated = 0

    # this is a special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used and when create instance of a class
    # change account number, sort code, account type, pin
    # sets the initial attributes of the object
    def __init__(self, initial_amount, firstname, lastname):
        # self.first_name = firstname
        # self.first_name = lastname
        # super().__init__(firstname, lastname, age, account_type)
        # _balance is an attribute, it's piece of data
        # self is an object pointer: points to whoever bank account who we are calling at that moment
        # _ is an identifier which is special
        self._balance = initial_amount
        self.first_name = str(firstname)
        # donder on fields means PRIVATE - KEEP OUT
        self.__last_name = str(lastname)
        self.pin = self.generate_random_pin()
        Account.numCreated += 1

    def generate_random_pin(self):
        random_pin = str(randint(1000, 9999))
        self.pin = random_pin
        return random_pin

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    # def __init__(self, account_holder, balance=0):
    #     self.account_holder = account_holder
    #     self.balance = balance

    # method = functionality - incorporating behaviour, encapsulating the primary behaviours of the bank account
    # _ python way to not view this when the function is called
    # _ single underscore means this field is semi private
    def deposit(self, amount):
        self._balance += amount
        # can add up to a certain amount to the account

    # functionality method
    def withdraw(self, amount):
        self._balance -= amount
        # validation
        if amount >= 0:
            self._balance -= amount

            # def withdraw(self, amount):
            #     if amount <= self.balance:
            #         self.balance -= amount
            #     else:
            #         print("Insufficient funds!")
            #     return self.balance

    # this is what Java calls a getter
    # Java uses these to retrieve attribute
    # data retrieval method
    def getbalance(self):
        return self._balance

    # create a getter method to retrieve first_name attribute (retrieve bank account holders name)
    def get_firstname(self):
        return self.first_name

    # create a getter method to retrieve the last_name attribute
    def get_lastname(self):
        return self.__last_name

    # setters: set or write a piece of information
    # getters READ and setters WRITE
    # setters have parameters
    # getters RETURN something, setters do not
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    # getters can translate or modify the data before returning it
    # setters often validate incoming data
    # setters often contain if statements

    # ADDED DISPLAY
    def __str__(self):
        return f"Account\nFirstname: {self.get_firstname()}\nLastname: {self.get_lastname()}" \
               f"\nBalance: ${self.getbalance()}\nPin:{self.pin}\n{'*' * 25}"
