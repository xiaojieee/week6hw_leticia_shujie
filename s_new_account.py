import pwinput
# Exercise
# Everything under class is indented
# it's a collection of attributes and methods


class Account:
    numCreated = 0

    # this is special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used
    def __init__(self, initial_amount, firstname, lastname, pin):
        # _balance is an attribute, it's a piece of data
        # things that start with _ underscore signify it's private
        # a single underscore is semi-private
        # double underscore is fully private
        self._balance = initial_amount
        self.first_name = firstname
        self.__last_name = lastname
        self.__pin = pin
        # the dunder on a field means PRIVATE - KEEP OUT
        # this is encapsulation
        # hiding stuff is good, you need to hide a good amount of stuff
        # this means they can't append the stuff, you're telling your co-workers to not touch this or change it
        Account.numCreated += 1

    # this is method
    def deposit(self, amount, pin):
        if amount >= 0 and pin == self.__pin:
            self._balance += amount
        # return - this return is not needed
        # if I make a deposit it will just add onto the balance
        # if I deposit a negative amount of money it will not take into account

    # this is method
    def withdraw(self, amount, pin):
        if amount >= 0 and pin == self.__pin:
            # this stops from withdraw a negative amount
            self._balance -= amount
        # return - this not needed either
        # if I take money out, it will take away from the balance

    # this is what Java calls a "getter"
    # Java uses these to retrieve attribute values
    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance

    # create a getter method to retrieve the first_name attribute
    def get_firstname(self):
        return self.first_name
    # getter is to get something

    def get_lastname(self):
        return self.__last_name

    # there's getters and setters
    # getters READ and setters WRITE
    # getters RETURN something, setters do not
    # setter is to set or write a piece of information
    # setters have parameters
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    # getters can translate or modify the data before returning it, e.g. uppercase, lowercase
    # setters often validate the incoming data
    # you would never make a setter for balance
    # setters often contains if statement

# there must be a mechanism that can indentify who's using this piece of code
# this 'template' can be used by everyone#
# this is what the 'self' job is
# every object orientation language will have a 'self', other languages will hide it
# zero parameter that is 'self'

# overriding a built-method
    def __str__(self):
        pin = int(pwinput.pwinput("Enter your pin:"))
        if pin == self.__pin:
            return (f"Account\nFirst Name: {self.get_firstname()}\nLast Name: {self.get_lastname()}"
                    f"\nBalance: ${self.get_balance(pin)}\n--------------------------")
        else:
            return f"Incorrect pin for {self.get_firstname()}"
