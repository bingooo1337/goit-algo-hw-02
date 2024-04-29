from queue import Queue
import random
import string

# Завдання 1

# Потрібно розробити програму, яка імітує приймання й обробку заявок:
# програма має автоматично генерувати нові заявки (ідентифіковані
# унікальним номером або іншими даними), додавати їх до черги,
# а потім послідовно видаляти з черги для "обробки",
# імітуючи таким чином роботу сервісного центру.

# Створити чергу заявок
queue = Queue()


def get_random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 25)))


def generate_request():
    # Створити нову заявку
    request = get_random_string()
    # Додати заявку до черги
    queue.put(request)
    print("Request generated:", request)


def process_request():
    # Якщо черга не пуста:
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        # Обробити заявку
        print("Request processed:", request)

    # Інакше:
    else:
        # Вивести повідомлення, що черга пуста
        print("Queue is empty")


while True:
    user_input = input("Generate/Process? ===> ").lower()

    if user_input == "generate":
        generate_request()
    elif user_input == "process":
        process_request()
    elif user_input == "exit":
        break
