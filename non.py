from random import randint
print('--------------------')
print('Добро пожаловать в числовую угадайку.')

# Функция случайного цифра
def rand_num():
    return randint(1, 100)

# Функция проверки
def is_viled(s):
    return s.isdigit() and 1 < int(s) < 100

# Функция игры
def guessing_number():
    print('Я загадаю число от 1 до 100, вам потребуется угадать это число')
    for _ in range(3):
        print('.....')
    print('...Я загадала число')    
    count = 0
    flag = True
    num = rand_num()
    
    #Бесконечный цикл с флагом
    while flag == True:
        n = input('Введите число: ')
        if n == 'break':
            break

        if not is_viled(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        
        n = int(n)
        count += 1

        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:    
            print(f'Вы угадали, поздравляем! Количество попыток {count}.')
            
            # Конец цикла
            flag = False

# Функция повтора
def repeat():
    s = input('Хотите повторить еще раз? (Да/Нет): ')            
    if s.lower() == 'да':
        return True
    else:
        return False

# Вызов функции
while True:
    guessing_number()
    if repeat():
        continue
    else:
        break
    