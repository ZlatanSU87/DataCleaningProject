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


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return random_array



# #Run benchmarking to score effectiveness of all algorithms
# print('Run benchmarking for random_predict: ', end='')
# score_game(random_predict)

# print('Run benchmarking for game_core_v2: ', end='')
# score_game(game_core_v2)

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
 
    count = 0
    max_number = 101
    min_number = 1
    current_number = 0
    
    while True:
        count += 1
        mid_number = (max_number + min_number) // 2
        if mid_number > number:
            max_number = mid_number
        elif mid_number < number:
            min_number = mid_number
        elif mid_number == number:
            break
    return count
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)


# def game_core_v3(number: int = 1) -> int:
#     """Устанавливаем верхнюю и нижнюю границы поиска, алгоритм угадывает число по принципу бинарного дерева,
#     если число больше центрального числа в диапазоне поиска, тогда переопределяем нижнюю границу,
#     она становится равной загаданному числу, если число меньше, то переопределяем вернюю границу,
#     и так каждый раз сокращаем диапазон поска в два раза.
#     Функция принимает загаданной число, и возвращает количество попыток.
    
#     Args:
#         number (int, optional): Загаданное число. Defaults to 1.

#     Returns:
#         int: Число попыток
#     """
#     # Ваш код начинается здесь
#     count = 0
#     max_num = 101 # Верняя граница поиска
#     min_num =1 # Нижняя граница поиска
    
#     while True:
#         count +=1  
#         mid = (max_num+min_num) // 2 # Находим центральное число в диапазоне
#         if number == mid:
#             break
#         elif mid < number:
#             min_num = mid
#         else:
#             max_num = mid        
#     # Ваш код заканчивается здесь
    
#     return count   
# print('Run benchmarking for game_core_v3: ', end='')
# score_game(game_core_v3)