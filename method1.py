class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_balance = 0

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

    def make_deposit(self, amount):
        self.user_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.user_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.first_name}, Balance: {self.user_balance}")
        return self



robert = User("Robert", "Seffens", 38)
jennifer = User("Jennifer", "Anniston", 53)
rachel = User("Racheal", "Green", 25)


robert.make_deposit(50).make_deposit(150).make_deposit(200).make_withdrawl(125).display_user_balance()
jennifer.make_deposit(20000000).make_deposit(350050).make_withdrawl(3500000).make_withdrawl(5).display_user_balance()
rachel.make_deposit(2500).make_withdrawl(300).make_withdrawl(2100).make_withdrawl(99).display_user_balance()

# robert.greeting()

# robert.make_deposit(50)
# robert.make_deposit(150)
# robert.make_deposit(200)
# robert.make_withdrawl(125)
# robert.display_user_balance()
# # 


# jennifer.make_deposit(20000000)
# jennifer.make_deposit(350050)
# jennifer.make_withdrawl(3500000)
# jennifer.make_withdrawl(5)
# jennifer.display_user_balance()

# rachel.make_deposit(2500)
# rachel.make_withdrawl(300)
# rachel.make_withdrawl(2100)
# rachel.make_withdrawl(99)
# rachel.display_user_balance()