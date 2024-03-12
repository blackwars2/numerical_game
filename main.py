import random as a

print("Добро пожаловать в числовую угадайку")
b = int(input("Введите до какого числа вы хотите угадывать?: "))
a = a.randint(1, b)


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

def game():
    print("Введи целое число от 1 до", b)
    count = 0
    while True:
        n = input()
        count += 1
        if is_valid(n):
            n = int(n)
            if n == a:
                print("Вы угадали число!!!")
                print("Количество попыток: ", count)
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...'")
                break
                game_return()
            elif n > a:
                print("Вы ввели число больше ")
            elif n < a:
                print("Вы ввели число меньше ")
        else:
            print("Введи нормальное число!")
            continue

game() #Запуск игры
def game_return():   # Функция повторного запуска
    while True:
        w = input('Хотите сыграть ещё раз? (Да / Нет): ')  # Запуск повторной игры
        if w.lower() == 'да' or w.lower() == 'lf' or w.lower() == 'da':
            game()
        else:
            print('Ну Хорошо, успехов тебе')
            break
game_return() #Повторный запуск
