import logging, time,random
logging.basicConfig(filename="sample.log", level=logging.INFO)
try:     #Для проверки чилового значения n,k
    f=int(input("Введите верхний границу диапозона чисел "))
    logging.info(f'Пользователь ввёл верхнюю границу диапозона чисел: {f} -{time.ctime()}')
    k=int(input('Введите количество попыток '))
    logging.info(f'Пользователь ввёл количество попыток: {k} -{time.ctime()}')
except:
    print('Нужны натуральные значения')
    logging.error(f"Введены не целые числа! -{time.ctime()}")
    quit()
if f<1 or k<1:     #Для проверки чилового значения n,k
    print('Нужны натуральные значения')
    logging.error(f"Введено целое не натуральное число! -{time.ctime()}")
    quit()
n=random.randint(1,f)
logging.info(f'Компьютер выбрал ответ: {n} -{time.ctime()}')
for i in range(k):   #Для ввода чисел и их проверки с искомым за k попыток
    a=int(input('Введите число '))
    logging.info(f'Попытка:{i+1} пользователь ввёл: {a} -{time.ctime()}')
    if a<n:
        print('Искомое значение больше')
        logging.info(f'Пользователь ввёл меньшее значение -{time.ctime()}')
    elif a>n:
        print('Искомое значение меньше')
        logging.info(f'Пользователь ввёл большее значение -{time.ctime()}')
    else: 
        print('Вы угадали')
        logging.info(f'Пользователь ввёл верное значение -{time.ctime()}')
        break
    if i+1==k:
        print('Попытки закончились')
        logging.info(f'Количество попыток закончилось -{time.ctime()}')
