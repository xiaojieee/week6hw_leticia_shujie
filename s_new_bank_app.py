from s_new_account import Account

# print(dir(Account)) - using this can check what's in the file and what can be used

# instantiation
# this is when we create objects based on classes

lisa_account = Account(100, 'Lisa', 'Simpson', 1234)
print(lisa_account)
# returns <account.Account object at 0x00000260DDB91970>
# account is the module
# there's a bank account object siting in the memory (the numbers)

# add some cash to Lisa's account
# OOP notation: object.method()
lisa_account.deposit(20, 1234)
# using the deposit method to add more money in the account

lastname = lisa_account.get_lastname()

lisa_account.set_lastname("Van Houten")
print(lisa_account)

# instantiate an account for Bart Simpson and experiment with it

bart_account = Account(900, 'Bart', 'Simpson', 2345)
print(bart_account)
bart_balance = bart_account.get_balance(2345)

bart_account.withdraw(423, 2645)

bart_account.deposit(82, 2345)
bart_account.deposit(80, 2345)
bart_account.deposit(10, 9999)

print(bart_account)


Marge_account = Account(20, 'Marge', 'Bouvier', 1111)

print(Marge_account)
