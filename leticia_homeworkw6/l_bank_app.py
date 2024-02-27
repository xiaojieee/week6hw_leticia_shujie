from l_new_account import Account

# print(dir(Account)) - using this can check what's in the file and what can be used

# todo: write the process
#  to do instanciation (look at notes and check)
# calling a class will call specific code to construct and instantiates an object
# the parameters passed is init amount, name and pin
# returns <account.Account object at 0x00000260DDB91970> without stringification function as
# object references are not printable
# account is the module
# there's a bank account object siting in the memory (the numbers)
# account_object 1
denis_account = Account(500, 'Denis', 'Sequeira', 1234)
# calling a method (function) for user to deposit an amount
denis_account.input_pin()
denis_account.deposit(20, 1234)
updated_balance = denis_account.get_balance(1234)
# python variables are references to objects
# Print the account details
print(denis_account)
new_last_name = denis_account.set_lastname("Alves")
lastname = denis_account.get_lastname()
print(denis_account)
# account_object 2
leticia_account = Account(600, 'Leticia', 'Santos', 6354)
leticia_account.input_pin()
withdraw_leticia = leticia_account.withdraw(700, 6354)
withdraw1_leticia = leticia_account.withdraw(200, 6354)
print(leticia_account)

# Second Account object
john_account = Account(1000, 'John', 'Doe', 1234)
# john_account.input_pin()
print(john_account)

# Third Account object
emma_account = Account(200, 'Emma', 'Johnson', 9876)
# emma_account.input_pin()
print(emma_account)

# Fourth Account object
michael_account = Account(800, 'Michael', 'Smith', 2468)
# michael_account.input_pin()
print(michael_account)
# prints the object
print(Account.numCreated)
# add some cash to Lisa's account
# OOP notation: object.method()
# using the deposit method to add more money in the account


print(f"{'-' * 25}")
# hasattr function used to check whether an object has a particular object or not
# takes two parameters: the object and the name of the attribute.
# If the attribute exists, it returns boolean values (TRUE OR FALSE)
# this code checks if 'Account' class has the __str__ method
print(hasattr(Account, '__str__'))
#   TODO Ask Victoria about how to check for methods
print(hasattr(Account, 'self.first_name'))
x = hasattr(Account, 'firstname')
print(x)

# W3 SCHOOLS EXAMPLE
# class Person:
#     name = "John"
#     age = 36
#     country = "Norway"
#
#
# x = hasattr(Person, 'age')
# print(x)

