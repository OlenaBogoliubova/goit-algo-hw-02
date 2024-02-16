import queue
import threading
import time

# Створення черги заявок
request_queue = queue.Queue()

# Флаг для виходу з програми
exit_flag = False

# Функція для генерації заявок і додавання їх до черги


def generate_request():
    request_id = 1
    while not exit_flag:
        request_data = f"Заявка {request_id}"
        request_queue.put(request_data)
        print(f"Заявка {request_id} додана до черги.")
        request_id += 1
        time.sleep(2)  # Затримка для імітації генерації заявок
    print("Завершення потоку генерації.")

# Функція для обробки заявок


def process_request():
    while not exit_flag:
        try:
            request_data = request_queue.get_nowait()
            print(f"Обробка заявки: {request_data}")
            # Видалення заявки після обробки
            request_queue.task_done()
        except queue.Empty:
            print("Черга порожня. Очікую нові заявки.")
            time.sleep(1)
    print("Завершення потоку обробки.")


# Головний цикл програми
if __name__ == "__main__":
    # Створення та запуск окремих потоків для генерації та обробки заявок
    generator_thread = threading.Thread(target=generate_request, daemon=True)
    processor_thread = threading.Thread(target=process_request, daemon=True)

    generator_thread.start()
    processor_thread.start()

# Очікування введення користувача для виходу з програми
try:
    input("Натисніть Enter для завершення програми.")
except KeyboardInterrupt:
    print("\n Завершення програми по вимозі користувача.")

    # Встановлення флага для виходу з циклів генерації та обробки
    exit_flag = True

    # Очікування завершення виконання потоків
    generator_thread.join()
    processor_thread.join()
