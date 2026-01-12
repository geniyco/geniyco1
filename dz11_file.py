
# 1. Склад інгредієнтів (Назва: Кількість грам/штук)
inventory = {
    "dough": 5000, "tomato_sauce": 2000, "cheese": 2000,
    "pepperoni": 500,
    "lettuce": 1000, "chicken": 1000, "croutons": 500,
    "parmesan": 200,
    "meat": 0  # Додано для обробки бургера
}

# 2. Основне меню
basic_menu = {
    "Pizza Pepperoni": {"price": 250, "ingredients": {"dough":
                                                          300, "tomato_sauce": 100, "cheese": 150, "pepperoni": 50}},
    "Caesar Salad": {"price": 180, "ingredients": {"lettuce":
                                                       200, "chicken": 150, "croutons": 50, "parmesan": 30}},
    "Water": {"price": 30, "ingredients": {}}
}

# 3. Сезонне меню (Спеціальні пропозиції)
specials_menu = {
    "Cheese Pizza": {"price": 200, "ingredients": {"dough":
                                                       300, "tomato_sauce": 100, "cheese": 250}},
    "Double Burger": {"price": 300, "ingredients": {"dough":
                                                        100, "meat": 300}}  # Увага: м'яса немає на складі!
}

# --- Етап 1: Ініціалізація та Злиття (Merges & Setup) ---

# Об'єднання меню за допомогою оператора розпакування **
full_menu = {**basic_menu, **specials_menu}

# Підготовка столиків (1-5) за допомогою dict.fromkeys()
# Примітка: використання порожнього словника як значення за замовчуванням може призвести до небажаної спільної посилання
# краще ініціалізувати пізніше або використовувати інший підхід для реального застосування, але для завдання використовуємо цей:
tables = dict.fromkeys(range(1, 6), [])
# Створюємо копії списків, щоб уникнути спільного посилання
tables = {k: list(v) for k, v in tables.items()}

# Аналітика комбо: Створюємо порожній словник combo_stats
combo_stats = {}


# --- Етап 2: Прийом замовлень (Logic, any/all, setdefault) & Етап 3 (Frozenset logic added) ---

def add_order(table_number, dish_name):
    # 1. Перевіряє наявність страви (in)
    if dish_name not in full_menu:
        print(f"❌ Страви '{dish_name}' немає в меню.")
        return False

    dish_info = full_menu[dish_name]
    ingredients = dish_info["ingredients"]

    # 2. Перевіряє наявність інгредієнтів (all + generator)
    ingredients_available = all(
        inventory.get(ingredient, 0) >= quantity for ingredient, quantity in ingredients.items()
    )

    if not ingredients_available:
        print(f"❌ На складі недостатньо інгредієнтів для приготування '{dish_name}'.")
        return False

    # 3. Списує інгредієнти зі складу
    for ingredient, quantity in ingredients.items():
        inventory[ingredient] -= quantity

    # 4. Додає страву до столика та оновлює combo_stats
    # setdefault тут не потрібен, оскільки tables ініціалізовано
    tables[table_number].append(dish_name)

    # Оновлення combo_stats за допомогою frozenset (Етап 3)
    current_combo = frozenset(tables[table_number])
    combo_stats[current_combo] = combo_stats.get(current_combo, 0) + 1

    print(f"✅ Замовлення: '{dish_name}' додано до столика {table_number}.")
    return True


# --- Етап 3: Аналіз та Фільтрація (Comprehensions) ---

# Створення veg_menu через dict comprehension з використанням not any()
meat_ingredients = {"pepperoni", "chicken", "meat"}
veg_menu = {
    dish_name: dish_info
    for dish_name, dish_info in full_menu.items()
    if not any(
        ingredient in meat_ingredients for ingredient in dish_info["ingredients"]
    )
}


# --- Етап 4: Закриття чека (Pop, Keys/Values) ---

def close_table(table_number):
    if table_number not in tables or not tables[table_number]:
        print(f"ℹ️ Столик {table_number} зараз порожній або не існує.")
        return

    # Використовує pop() для отримання замовлень та "очищення" столика
    orders = tables.pop(table_number)

    total_amount = 0
    print(f"\n--- Чек для столика {table_number} ---")
    for dish_name in orders:
        price = full_menu[dish_name]["price"]
        print(f"- {dish_name}: {price} грн")
        total_amount += price

    print(f"--------------------------------")
    print(f"Загальна сума: {total_amount} грн")
    print(f"--------------------------------\n")

    # Повертаємо столик у початковий порожній стан для подальших замовлень
    tables[table_number] = []


# --- Приклад сценарію (Test Case) ---

print("--- Запуск тестового сценарію ---")

# 2. Клієнт замовив Піцу на столик 1
add_order(1, "Pizza Pepperoni")

# 3. Клієнт замовив Воду на столик 1
add_order(1, "Water")

# 4. Спроба замовити Бургер (має спрацювати повідомлення про відсутність м'яса)
add_order(2, "Double Burger")

# 5. Друк вег-меню
print("\n--- Вегетаріанське меню ---")
print(veg_menu)

# 6. Закриття столика 1
close_table(1)

print("\n--- Поточний стан складу ---")
print(inventory)

print("\n--- Статистика комбо ---")
print(combo_stats)