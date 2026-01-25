class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Пополнение прошло успешно")

    def show_balance(self):
        print(f"Баланс: {self.__balance}")


class CheckingAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Пополнение на расчетный счет прошло успешо")


