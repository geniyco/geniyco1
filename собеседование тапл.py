
data = [(1, 2), (4, 5), (2, 1), (3, 3), (5, 4)]

def filter_pairs(pairs_list):
    unique_pairs = []
    for pair in pairs_list:
        mirror_pair = tuple(reversed(pair))

        # Перевіряємо, чи немає в результаті ні самої пари, ні її дзеркала
        if pair not in unique_pairs and mirror_pair not in unique_pairs:
            unique_pairs.append(pair)

    return unique_pairs

# Перевірка результату
result = filter_pairs(data)
print(f"Вхідні дані: {data}")
print(f"Очікуваний результат: [(1, 2), (4, 5), (3, 3)] (порядок не важливий)")
print(f"Отриманий результат: {result}")