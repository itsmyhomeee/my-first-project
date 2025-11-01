#алгоритм обработки пользовательского имени

import re

rules = re.compile(r'([а-яА-ЯёЁ])|([^a-zA-Z])')
def username():
    while True:
        word = str(input("Введите ваше имя на русском языке")).strip(" ")

        answer = bool(rules.match(word))
        if answer == True:
            return word

        print("Ошибка! Имя должно содержать только русские буквы")
user_name = username()

print(f"Приятно познакомиться, {user_name}!")


#пароль из 4х цифр



def check():
    r_password = re.compile(r'[9]{4}]')
    password = input("Come up with a new password")

    password2 = input("Enter your password")
    r_password.search(password)
    while r_password.search(password2):
        if password == password2:
            return "Welcome"
        else:
            print("Invalid password")

        return f"Добро пожаловать, {user_name}!"
    print("Введи пароль еше раз")



print(check())