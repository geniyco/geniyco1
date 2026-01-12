"""5------------------------------------------------------------------------------------------------------"""
import string

def is_pangram(text):
    """
    Проверяет, содержит ли заданный текст все буквы английского алфавита.
    Игнорирует регистр, пробелы, цифры и знаки препинания.
    """
    # 1. Определяем множество всех букв английского алфавита
    alphabet_set = set(string.ascii_lowercase)
    # 2. Создаем множество букв из входного текста
    #    - Приводим весь текст в нижний регистр (.lower())
    #    - Оставляем только те символы, которые являются буквами (c.isalpha())
    text_set = set("".join(c for c in text if c.isalpha()).lower())
    # 3. Проверяем, является ли алфавит подмножеством букв в тексте (возвращает True/False)
    return alphabet_set.issubset(text_set)
# --- Примеры использования ---
text_true = "The quick brown fox jumps over the lazy dog."
text_false = "Hello, world!"
print(f"'{text_true}' является панграммой? -> {is_pangram(text_true)}")
print(f"'{text_false}' является панграммой? -> {is_pangram(text_false)}")

"""1------------------------------------------------------------------------------------------------------"""
groom_guests = {"Ivan", "Petro", "Olga", "Darka"}
bride_guests = {"Maria", "Darka", "Ivan", "Oksana"}


union_set = groom_guests | bride_guests
print(union_set)
"""2------------------------------------------------------------------------------------------------------"""
anton = {"GoT", "Chernobyl", "Friends"}
boris = {"Friends", "Office", "Chernobyl"}

s_diff_set = anton ^ boris
print(s_diff_set)
"""3------------------------------------------------------------------------------------------------------"""
def check_admin_access(user_perms, requierd_perms):
    return requierd_perms <= user_perms

required_permissions = {"edit", "delete", "publish"}
user_permissions = {"connect", "view", "edit", "publish"}

# Виклик функції з наданими даними
print(f"{check_admin_access(user_permissions, required_permissions)}")
"""4------------------------------------------------------------------------------------------------------"""
def moderate_message(text):
    banned_words = {"buy", "crypto", "free", "click"}
    message_words = set(text.lower().split())
    if message_words.intersection(banned_words):
        return False
    else:
        return True
input_text = "Hello friend click here for free crypto"
is_allowed = moderate_message(input_text)
print(f"Сообщение '{input_text}' разрешено? -> {is_allowed}")  # Вывод: False


