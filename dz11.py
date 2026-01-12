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
import copy

# Входные данные
default_settings = {
    "theme": "light",
    "notifications": {"email": True, "sms": False},
    "limit": 50
}
user_preferences = {
    "theme": "dark",
    "limit": 100
}

print("--- Исходные данные ---")
print(f"Default: {default_settings}")
print(f"User Prefs: {user_preferences}\n")

# Задание 1: Объединение с помощью оператора ** (распаковка)
final_config = {**default_settings, **user_preferences}
print("--- 1. Результат слияния (Shallow Merge) ---")
print(f"Final Config: {final_config}\n")

# Задание 2: Изменение SMS-уведомлений
final_config["notifications"]["sms"] = True
print("--- 2. Final Config после изменения SMS ---")
print(f"Final Config: {final_config}\n")

# Задание 3: Демонстрация shallow vs deep copy
print("--- 3. Демонстрация Copy Types ---")

# 3.1. Поверхностное копирование с помощью .copy()
shallow_copy = final_config.copy()
shallow_copy["notifications"]["sms"] = False
print(f"Оригинал после shallow copy: {final_config['notifications']['sms']} (Оригинал изменился!)")

# 3.2. Глубокое копирование с помощью copy.deepcopy()
deep_copy = copy.deepcopy(final_config)
deep_copy["notifications"]["sms"] = True
print(f"Оригинал после deep copy: {final_config['notifications']['sms']} (Оригинал не изменился)\n")
"""----------------------------------------------------------------------------------------------------"""
matches = [
    (["Ivan", "Petro"], 10),
    (["Petro", "Ivan"], 5),
    (["Alex", "Oleg"], 12),
    (["Oleg", "Alex"], 8)
]

team_scores = {}

for team_list, score in matches:
    team_key = frozenset(team_list)
    team_scores[team_key] = team_scores.setdefault(team_key, 0) + score

print("Результати змагань:")
for team_frozenset, total_score in team_scores.items():
    team_names = list(team_frozenset)
    print(f"Команда {team_names}: {total_score} очок")