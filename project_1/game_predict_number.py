import numpy as np

# def random_predict(number: int = 1) -> int:
#     """Просто угадываем на random, никак не используя информацию о больше или меньше.
#        Функция принимает загаданное число и возвращает число попыток

#     Args:
#         number (int, optional): Загаданное число. Defaults to 1.

#     Returns:
#         int: Число попыток
#     """
#     count = 0

#     while True:
#         count += 1
#         predict_number = np.random.randint(1, 101)  # предполагаемое число
#         if number == predict_number:
#             break  # выход из цикла если угадали
    
#     return count
# print(random_predict())

# def game_core_v2(number: int = 1) -> int:
#     """Сначала устанавливаем любое random число, а потом уменьшаем
#     или увеличиваем его в зависимости от того, больше оно или меньше нужного.
#        Функция принимает загаданное число и возвращает число попыток
       
#     Args:
#         number (int, optional): Загаданное число. Defaults to 1.

#     Returns:
#         int: Число попыток
#     """
#     count = 0
#     predict = np.random.randint(1, 101)
    
#     while number != predict:
#         count += 1
#         if number > predict:
#             predict += 1
#         elif number < predict:
#             predict -= 1

#     return count


# def score_game(random_predict) -> int:
#     """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

#     Args:
#         random_predict ([type]): функция угадывания

#     Returns:
#         int: среднее количество попыток
#     """
#     count_ls = []
#     np.random.seed(1)  # фиксируем сид для воспроизводимости
#     random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

#     for number in random_array:
#         count_ls.append(random_predict(number))

#     score = int(np.mean(count_ls))
#     print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
#     return random_array



# #Run benchmarking to score effectiveness of all algorithms
# print('Run benchmarking for random_predict: ', end='')
# score_game(random_predict)

# print('Run benchmarking for game_core_v2: ', end='')
# score_game(game_core_v2)

# def game_core_v3(number: int = 1) -> int:
#     """
#     Вводим переменные под верхнюю и нижнюю границу поиска. Определяем путём вычисления центральное число в диапозоне границ.
#     Если центральное число больше угадываемого, то присваиваем центральное чило нижней границе; если меньше - присваиваем
#     его верхней границе. И так работает цикл While, пока не найдёт нужное число. В среднем - получается 5 попыток, при верхней
#     планке в 20. Задача решена.
#     Args:
#         number (int, optional): Загаданное число. Defaults to 1.

#     Returns:
#         int: Число попыток
#     """
#     count = 0
#     max_number = 101
#     min_number = 1
    
#     while True:
#         count += 1
#         mid_number = (max_number + min_number) // 2
#         if mid_number > number:
#             max_number = mid_number
#         elif mid_number < number:
#             min_number = mid_number
#         elif mid_number == number:
#             break
#     return count
# score_game(game_core_v3)
# print('Run benchmarking for game_core_v3: ', end='')

import numpy as np

def loocking_number(number: int = 25) -> int:
    
    """ Сначала устанавливаем random число, а потом уменьшаем
        или увеличиваем его в половину дельты границ проверок взависимости 
        от того, больше оно или меньше нужного.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 25.
    Returns:
        int: Число попыток
    """
    
    predict_current = np.random.randint (1, 101)
    
    predict_max = 101
    predict_min = 0
    
    count = 1 #не ноль, что-бы при угадывании с первой попытки функция вернула 1
        
    while True:
        if predict_current == number:
            break
        elif predict_current > number:
            predict_max = predict_current
            predict_current -= int((predict_max - predict_min) // 2)
        else:
            predict_min = predict_current
            predict_current += int((predict_max - predict_min) // 2)
        count += 1   
    
    return count
    

def count_attempt(loocking_number):
    """ Функция для сбора статистики расчетов нашего когда.
        Принимает функцию, выдает сообщение о максимальном, минимальном и среднем
        количестве результатов выполнения нашего кода за 1000 запусков
    """
    
    count_lst = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:   
        count_lst.append(loocking_number(number))
    
    print(f'Среднее число попыток {int(np.mean(count_lst))}') # Ожидаемо 6
    print(f'Максимальное количество попыток {max(count_lst)}') # Ожидаемо 8
    print(f'Минимальное количество попыток {min(count_lst)}') # Ожидаемо 1