"""------------------------------------------------------------------------------------------------------"""
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

for x in frange(0.5, 2.0, 0.5):
    print(x)
"""------------------------------------------------------------------------------------------------------"""
def running_sum(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total

input_list = [10, 5, 20, 1]
for x in running_sum(input_list):
    print(x)
"""------------------------------------------------------------------------------------------------------"""
def parse_csv(lines):
    lines_iter = iter(lines)
    keys = [key.strip() for key in next(lines_iter).split(',')]

    for line in lines_iter:
        values = [value.strip() for value in line.split(',')]
        yield dict(zip(keys, values))

csv_data = [
    "id, name, age",
    "1, Oleg, 25",
    "2, Maria, 30",
    "3, Ivan, 19"
]

for row_dict in parse_csv(csv_data):
    print(row_dict)
"""------------------------------------------------------------------------------------------------------"""
cart = [
    {"name": "Laptop", "price": 1200, "category": "Tech"},
    {"name": "Book", "price": 15, "category": "Education"},
    {"name": "Mouse", "price": 50, "category": "Tech"},
    {"name": "Course", "price": 200, "category": "Education"},
    {"name": "Pen", "price": 2, "category": "Office"}
]

# 1. Filter: Залишити тільки товари, що коштують більше 20 доларів
# filter() приймає функцію (тут lambda) та ітерабельний об'єкт.
# Вона повертає ітератор, який ми перетворюємо на список.
filtered_cart_func = list(filter(lambda item: item["price"] > 20, cart))

# 2. Map: Перетворити ці об'єкти на список рядків формату
# map() приймає функцію перетворення та ітерабельний об'єкт.
mapped_cart_func = list(map(lambda item: f"({item['category']}): {item['name']} ${item['price']}", filtered_cart_func))

# 3. Sorted: Відсортувати ці рядки за алфавітом
sorted_cart_func = sorted(mapped_cart_func)

print("Відфільтрований, перетворений та відсортований список (функціональний підхід):")
for item in sorted_cart_func:
    print(item)
"""------------------------------------------------------------------------------------------------------"""
cart = [
    {"name": "Laptop", "price": 1200, "category": "Tech"},
    {"name": "Book", "price": 15, "category": "Education"},
    {"name": "Mouse", "price": 50, "category": "Tech"},
    {"name": "Course", "price": 200, "category": "Education"},
    {"name": "Pen", "price": 2, "category": "Office"}
]

# Етап 1: Фільтрація товарів дорожчих за $20
filtered_list = []
for i in cart:
    if i['price'] > 20:
        filtered_list.append(i)

# Етап 2: Перетворення відфільтрованих словників у відформатовані рядки
mapped_list = []
for x in filtered_list:
    formatted_string = f"({x['category']}): {x['name']} ${x['price']}"
    mapped_list.append(formatted_string)

# Етап 3: Сортування отриманого списку рядків за алфавітом
sorted_list = sorted(mapped_list)

print("Кінцевий результат виконання всіх етапів:")
for item in sorted_list:
    print(item)
"""------------------------------------------------------------------------------------------------------"""
words = ["apple", "zoo", "banana", "cat", "dog", "elephant"]

# Використовуємо lambda, щоб створити ключ сортування, який повертає кортеж:
# (довжина слова, саме слово)
sort_key = lambda x: (len(x), x)

# Передаємо цей ключ у функцію sorted()
sorted_words = sorted(words, key=sort_key)

print("Відсортований список слів:")
print(sorted_words)
"""------------------------------------------------------------------------------------------------------"""
def create_tag_wrapper(tag):
    """
    Приймає назву HTML-тегу і повертає нову функцію-обгортку (замикання).
    """

    def wrap(text):
        # Внутрішня функція, яка використовує 'tag' із зовнішньої області видимості
        return f"<{tag}>{text}</{tag}>"

    # Повертаємо саму функцію wrap як об'єкт
    return wrap


# Приклад використання, як у завданні:
bold_wrapper = create_tag_wrapper("b")
h1_wrapper = create_tag_wrapper("h1")

print(bold_wrapper("Hello"))
print(h1_wrapper("Title"))
"""------------------------------------------------------------------------------------------------------"""
def create_wallet():
    """
    Створює гаманець зі збереженням стану за допомогою замикання та nonlocal.
    """
    # Локальна змінна, стан якої ми зберігаємо
    balance = 0

    def add_money(amount):
        # Оголошуємо змінну 'balance' як nonlocal, щоб змінити її у батьківській функції
        nonlocal balance

        # 1. Додаємо amount до balance
        balance += amount

        # 2. Повертаємо поточний баланс
        return balance

    # Повертаємо саму функцію add_money (замикання)
    return add_money

my_wallet = create_wallet()

print(my_wallet(100)) # Очікуваний вивід: 100
print(my_wallet(50))  # Очікуваний вивід: 150
print(my_wallet(-20)) # Очікуваний вивід: 130
"""------------------------------------------------------------------------------------------------------"""
def fibonacci():
    # 1. Ініціалізація початкових значень (0, 1)
    a, b = 0, 1

    # 2. Створення нескінченного циклу, як вимагає умова
    while True:
        # 3. Повернення поточного числа (a)
        yield a

        # 4. Оновлення значень для наступної ітерації (Логіка: a, b = b, a + b)
        a, b = b, a + b


# --- Приклад використання з умови: ---
# Використання: Виведіть перші 10 чисел, використовуючи цикл з break або функцію next().

print("Перші 10 чисел Фібоначчі:")

# Варіант 1: Використання циклу for з break
count = 0
for number in fibonacci():
    print(number)
    count += 1
    if count >= 10:
        break

# Або Варіант 2: Використання функції next()
# gen = fibonacci()
# print(next(gen)) # 0
# print(next(gen)) # 1
# ...
"""------------------------------------------------------------------------------------------------------"""
import random
import string

# Набір символів для використання
characters = string.ascii_letters + string.digits


def password_generator(length, count):
    """
    Генератор, який створює задану кількість випадкових паролів вказаної довжини.
    """
    # Цикл, що повторюється 'count' разів
    for _ in range(count):
        # Генерація одного пароля потрібної довжини 'length'
        password = "".join([random.choice(characters) for _ in range(length)])

        # Повернення (віддача) згенерованого пароля
        yield password


# --- Приклад використання ---
print("Генерація 3 паролів довжиною 8 символів:")
gen = password_generator(length=8, count=3)
print(f"Пароль 1: {next(gen)}")
print(f"Пароль 2: {next(gen)}")
print(f"Пароль 3: {next(gen)}")



















