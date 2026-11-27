print("Введите имя")
name=input()
print("Привет", name)
print("В этой игре я помогу тебе решать примеры ")
action=input("Выбери действие (+, -, *, :): ")
print("Отлично, а теперь запиши числа")
a= int(input())
b= int(input()) 
if action == "+":
     print(f"Ответ: {a + b}")
elif action == "-":
     print(f"Ответ: {a - b}")
elif action == "*":
     print(f"Ответ: {a * b}")
elif action == ":":
     print(f"Ответ: {a / b}")
else:
     print("Я пока еще того не знаю")