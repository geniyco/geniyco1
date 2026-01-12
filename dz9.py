#3 без допомоги 7/10
cart = [
    ("Хліб", 25)
    ("Молоко", 35)
    ("Масло", 60)
    ("Цукерки", 120)
]
total = 0
def calculate_total(cart):
    for value in cart:
        total += value[0]
    return total

print(calculate_total(cart))
#3 з допомогою
cart = [
("Хліб", 25),
("Молоко", 35),
("Масло", 60),
("Цукерки", 120)
]

def calculate_total(cart):
    total_sum = 0
    for item in cart:
        total_sum += item[1] # Доступ до ціни за індексом 1
    return total_sum

# Перевірка результату
result = calculate_total(cart)
print(f"Загальна сума чека: {result}")
#4 сам 1/10
winning_numbers = (15, 23, 4, 8, 42, 16)
def check_ticket(number):
    if number in winning_numbers:
        print(f"{number} win")
    else:
        print(f"{number} lose")

print(check_ticket(123))
print(check_ticket(12))
print(check_ticket(15))
print(check_ticket(4))
print(check_ticket(65))
#4 з допомогою
winning_numbers = (15, 23, 4, 8, 42, 16)

def check_ticket(number):
    if number in winning_numbers:
        return "Виграш!"
    else:
        return "Спробуйте ще"

# Приклади використання функції:
print(f"Квиток 23: {check_ticket(23)}")
print(f"Квиток 5: {check_ticket(5)}")
print(f"Квиток 16: {check_ticket(16)}")