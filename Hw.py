
# def greet_user(name):
    #print(f"Привет, {name}! Добро пожаловать в мир Python!")


# def calculate_sum(a, b):
    #return a + b



# name = input("Введите ваше имя: ")
# greet_user(name)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# result = calculate_sum(num1, num2)
# print(f"Сумма чисел: {result}")


# from datetime import datetime


# birth_year = int(input("Введите год вашего рождения: "))


# current_year = datetime.now().year

# age = current_year - birth_year

# print(f"Ваш возраст: {age}")

# if age < 18:
    # print("Вы еще молоды, учеба — ваш путь!")
# elif 18 <= age <= 65:
    # print("Отличный возраст для карьерного роста!")
# else:
    # print("Пора наслаждаться заслуженным отдыхом!")



# n = int(input("Введи число:"))

# total = 0

# print("Числа", end =" ")
# for i in range(n + 1):
   # total += i

# print()

# print(f" Сумма чисел: {total}")



# def check_triangle(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
       # return "Треугольник построить нельзя."


    # if a == b == c:
       # return "Треугольник равносторонний."
    # elif a == b or a == c or b == c:
       # return "Треугольник равнобедренный."
    # else:
       # return "Треугольник разносторонний."


# a = int(input("Введите длину первой стороны: "))
# b = int(input("Введите длину второй стороны: "))
# c = int(input("Введите длину третьей стороны: "))

# result = check_triangle(a, b, c)
# print(f"Результат: {result}")



# def calculator():

   # def add(a, b):
       # return a + b

    # def subtract(a, b):
       # return a - b

    # def multiply(a, b):
       # return a * b

    # def divide(a, b):
       # if b == 0:
           # return "Ошибка: деление на ноль"
        # return a / b

    # a = int(input("Введите первое число: "))
    # b = int(input("Введите второе число: "))
    # operation = input("Выберите операцию (+, -, *, /): ")

    # if operation == "+":
       # return add(a, b)
    # elif operation == "-":
       # return subtract(a, b)
    # elif operation == "*":
       # return multiply(a, b)
    # elif operation == "/":
       # return divide(a, b)
    # else:
       # return "Неизвестная операция"


# result = calculator()
# print(f"Результат: {result}")


# Таблица умножения от 1 до 10

# for i in range(1, 11):
   # for j in range(1, 11):
       # print(i * j, end=" ")
    # print()



def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers




user_input = input("Введите числа через запятую: ")

numbers = [int(num.strip()) for num in user_input.split(",")]

sorted_numbers = bubble_sort(numbers)

print("Отсортированный список:", ", ".join(map(str, sorted_numbers)))

yeah


