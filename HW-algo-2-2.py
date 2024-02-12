import sys
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


if __name__ == "__main__":
    # Отримуємо рядок з командного рядка (перший аргумент, бо нульовий - назва скрипта)
    input_str = ' '.join(sys.argv[1:])

    if not input_str:
        print("Будь ласка, введіть рядок для перевірки паліндрому.")
    else:
        result = is_palindrome(input_str)
        if result:
            print(f'Рядок "{input_str}" - паліндром')
        else:
            print(f'Рядок "{input_str}" - не паліндром')
