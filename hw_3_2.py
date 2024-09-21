import random

def get_numbers_ticket(min=1, max=100, quantity=6):

    # Перевірка параметрів: якщо хоча б одна з умов не виконується, то повертаємо порожній список
    if not (1 <= min <= max <= 100) or not (0 < quantity <= (max - min + 1)):
        return []

    # Генерація унікальних чисел і сортування
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


print(get_numbers_ticket(1, 100, 6))   # Випадкові шість чисел між 1 і 100
print(get_numbers_ticket(10, 20, 6))    # Випадкові 6-ть чисел між 10 і 20
print(get_numbers_ticket(100, 50, 5))   # Невірні параметри, поверне []
