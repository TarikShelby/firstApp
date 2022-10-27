import random

random_number = random.randint(1, 3)
user_number = input("Угадай число : ")

if int(user_number) == random_number:
    print("Угадал поздравляю ")
else:
    print("Вы не угадали")
print(f"Число было {random_number}")