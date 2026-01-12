categories = ["Laptops", "Smartphones", "Tablets", "Accessories"]
inventory = dict.fromkeys(categories)

for key in inventory:
    inventory[key] = []
print(inventory)

shipment = [
    ("Laptops", "MacBook Air"),
    ("Smartphones", "iPhone 15"),
    ("Laptops", "Lenovo ThinkPad"),
    ("Accessories", "House"),
    ("Smartphones", "Samsung S24"),
    ("Fridges", "Bosch")
]

for category, item in shipment:
    inventory.setdefault(category, []).append(item)
print(inventory)

if "Tablets" in inventory and not inventory['Tablets']:
    del inventory['Tablets']
print(inventory)

"""-------------------------------------------------------------------------------"""
sessions = {
    "user_1": {"status": "active", "time": 10},
    "user_2": {"status": "disconnected", "time": 500},
    "user_3": {"status": "active", "time": 45},
    "user_4": {"status": "dead", "time": 9999},
    "user_5": {"status": "active", "time": 5},
}
spam_users = ["user_4", "user_99"]

print(f"Початковий словник: {sessions}\n")

# Завдання 1: Використовуючи pop(), видаліть користувачів, які є у списку spam_users.
print("--- Крок 1: Видалення спам-користувачів ---")
for user in spam_users:
    removed_status = sessions.pop(user, None)
    if removed_status:
        print(f"Видалено користувача: {user}")
    else:
        print(f"Користувача {user} немає в словнику (KeyError уникнено)")
print(f"Словник після видалення спамерів: {sessions}\n")

# Завдання 2: Використайте popitem(), щоб видалити останнього доданого користувача.
print("--- Крок 2: Видалення останнього користувача ---")
removed_user_item = sessions.popitem()
print(f"Видалено останнього доданого користувача: {removed_user_item}")
print(f"Словник після popitem(): {sessions}\n")

# Завдання 3: Знайдіть всі сесії, де status дорівнює "active". Зберіть імена цих користувачів (keys) в окремий список.
print("--- Крок 3: Пошук активних користувачів ---")
active_users_keys = []
for key, value in sessions.items():
    if value["status"] == "active":
        active_users_keys.append(key)
print(f"Список активних користувачів (ключі): {active_users_keys}\n")

# Завдання 4: Виведіть окремо список усіх значень часу (values), що залишилися в системі.
print("--- Крок 4: Збір значень часу ---")
remaining_times = [session_data["time"] for session_data in sessions.values()]
print(f"Список усіх значень часу, що залишилися: {remaining_times}\n")
"""----------------------------------------------------------------------------------------------------"""