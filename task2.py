from collections import deque

# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр,
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python),
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.


def is_palindrome(input):
    input = input.replace(" ", "").lower()

    queue = deque()
    # fill deque
    for c in input:
        queue.append(c)

    while len(queue) > 1:
        # compare
        if queue.popleft() != queue.pop():
            return False
    return True


user_input = input("Enter a string to check if it is a palindrome: ")
print("Is polindrome:", is_palindrome(user_input))
