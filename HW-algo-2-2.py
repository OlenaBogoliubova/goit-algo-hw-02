from collections import deque


def is_palindrome(input_str):
    # Перетворимо рядок у нижній регістр і видалимо пробіли
    cleaned_str = ''.join(input_str.lower().split())

    # Створимо двосторонню чергу (deque) з очищеного рядка
    char_queue = deque(cleaned_str)

    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


# Приклад використання:
input_str = "Я несу гусеня"
result = is_palindrome(input_str)

if result:
    print(f'Рядок "{input_str}" - паліндром')
else:
    print(f'Рядок "{input_str}" - не паліндром')
