import random
secret = random.randint(1, 10)
print("Я загадал число от 1 до 10. Попробуй угадать!")
guess = int(input("Введите число: "))
if guess == secret:
    print("Ура! Ты угадала!")
else:
    print("Не угадала! Я загадала число", secret)