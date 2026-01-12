# 1
name = str(input("Введіть ім'я: "))
age = int(input("Введіть скільки років: "))
print(f"Привіт {name}, через 5 років тобі буде {age + 5}")
#2
chuslo = int(input("Введіть число: "))
if chuslo % 2 == 0:
    print("парне")
else:
    print("не парне")
#3
num1 = int(input("Введіть число 1: "))
num2 = int(input("Введіть число 2: "))

znak = input("Введіть знак (*, / , +, -:")
if znak == "*":
    print(num1 * num2)
elif znak == "+":
    print(num1 + num2)
elif znak == "-":
    print(num1 - num2)
elif znak == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Помилка(ділення на 0)")
else:
    print("Ввідіть вірну дію")
#4
N = int(input("Введіть число: "))
for i in range(1, 11):
    result = N * i
    print(result)
#5
N = int(input("Введіть число: "))
j = 0
for i in range(1, N+1):
    j += i
print(j)
#6
list1 = []
for element in range(5):
    element = input("Введіть слово: ")
    list1.append(element)

print(list1)
#7
list1 = [4, 12, 8, 1, 25, 9]
max_number = list1[0]
for number in list1[1:]:
    if number > max_number:
        max_number = number
    # Виводимо результат
print(f"Найбільше число у списку: {max_number}")
#8
students = [60, 90, 45, 78, 30, 95, 55]
clear_spusok = []
for number in students:
    if number >= 60:
        clear_spusok.append(number)

print(clear_spusok)
#9
def greet_user(name, time_):
    print(f"Доброго {time_} {name} ")

greet_user("Леха ", "ранку")
greet_user("Леха ", "дня")
greet_user("Леха ", "вечора")
#10
def chusla(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

user_input_str = input("Введіть числа через пробіл: ")
try:
    user_numbers = [float(num) for num in user_input_str.split()]
    avarage = chusla(user_numbers)
    print(f"Середнє арифмитичне {avarage}")
except ValueError:
    print(f"Помилка ValueError")



