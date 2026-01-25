#       Functions

# name = "Alise"
# balance = 100

def create_account(name, balance=200):
    return print(f"Создан счет для {name} с балансом {balance}")

create_account(balance=100, name="bob")

print("-" * 30)


def create_account(name, *transactions):
    print(f"Создан счет для {name}")
    for transaction in transactions:
        print(f"Транзакция: {transaction}.")

create_account("bob", 100, 300, 500, -400)

print("-" * 30)

def create_account(name, **account_details):
    print(f"Создан счет для {name}")
    for detail, valuein in account_details.items():
        print(f"{detail}: {valuein}")

create_account("bob", initial_deposit=200, account_typa="Сбер счет")

print("-" * 30)

initial_deposit = 200  #Глобальная область - используется ток если нет ее изменений внутри функции

def create_account(name):
    initial_deposit = 100 # Локальная - может меняться внутри функции изменив значение глобальной
    print(f"Создан счет для {name} с балансом {initial_deposit}")

create_account("bob")

