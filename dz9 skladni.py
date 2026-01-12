#1 дуже складне 10/10
def compress_string(s):
    result = []
    if not s:
        return result

    current_char = s[0]
    count = 0

    for char in s:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    # Додаємо останній символ та його кількість
    result.append((current_char, count))
    return result


input_str = 'AAAABBBCCDAA'
compressed_list = compress_string(input_str)
print(f"Вхідний рядок: '{input_str}'")
print(f"Очікуваний вивід: [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]")
print(f"Отриманий вивід: {compressed_list}")

#2 З допомогою 10/10 складність логіка більше менше не зрозуміла(спробував сам)
schedule = [(9, 11), (13, 15), (16, 18)]

def can_schedule(existing_meetings, new_meeting):
    for a_start, a_end in existing_meetings:
        b_start, b_end = new_meeting
        if a_start < b_end and a_end > b_start:
            return False
    return True
print(f"{can_schedule(schedule, (40, 50))}")
print(f"{can_schedule(schedule, (10, 12))}")
print(f"{can_schedule(schedule, (11, 13))}")
#3 складність 10/10
import random
# Завдання 1: Генерація та перемішування колоди
def generate_deck():
    suits = ("Bubna", "Chervva", "Trefa", "Pika")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck
# Завдання 2: Підрахунок очок (якщо потрібно)
def calculate_score(hand):
    score = 0
    for rank, suit in hand:
        if rank.isdigit():
            score += int(rank)
        elif rank in ("J", "Q", "K"):
            score += 10
        elif rank == "A":
            score += 11
    return score
my_deck = generate_deck()
print(f"Кількість карт у колоді: {len(my_deck)}")
print(f"Перші 5 карт перемішаної колоди: {my_deck[:5]}")
test_hand = [('A', 'Pika'), ('K', 'Bubna'), ('5', 'Trefa')]
print(f"Очки в руці {test_hand}: {calculate_score(test_hand)}")
#4  10/10 +/- логіка зрозуміла але самостійно не зміг вирішити (спробував сам)
data = [(1, 2), (4, 5), (2, 1), (3, 3), (5, 4)]
def filter_pairs(pairs_list):
    tpl = []
    for pair in pairs_list:
        mirror_pair = tuple(reversed(pair))
        if pair not in tpl and mirror_pair not in tpl:
            tpl.append(pair)
    return tpl
result = filter_pairs(data)
print(data)
print(result)
