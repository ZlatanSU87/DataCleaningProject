from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import deque
import numpy as np
# # Создаём пустой объект Counter
# c = Counter()
# c['red'] += 1
# print(c)
# # Будет напечатано:
# # Counter({'red': 1})

# cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
# c = Counter()
# for car in cars:
#     c[car] += 1
 
# print(c)
# # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
# c = Counter(cars)
# print(c)
# # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
# print(c['black'])
# # 3
# print(c['purple'])
# # 0
# print(sum(c.values()))
# # 9
# print(c.values())
# # dict_values([3, 2, 3, 1])

# cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
# cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
# counter_moscow = Counter(cars_moscow)
# counter_spb = Counter(cars_spb)
 
# print(counter_moscow)
# print(counter_spb)
 
# # Counter({'black': 4, 'yellow': 3, 'white': 2})
# # Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
# print(counter_moscow + counter_spb)
# # Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})
# counter_moscow.subtract(counter_spb)
# print(counter_moscow)
# # Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

# # Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения
# # после функции subtract.
# counter_moscow = Counter(cars_moscow)
# counter_spb = Counter(cars_spb)
 
# print(counter_moscow - counter_spb)
# # Counter({'black': 2, 'yellow': 1})

# print(*counter_moscow.elements())
# # black black black black white white yellow yellow yellow

# print(list(counter_moscow))
# # ['black', 'white', 'yellow']

# print(dict(counter_moscow))
# # {'black': 4, 'white': 2, 'yellow': 3}

# print(counter_moscow.most_common())
# # [('black', 4), ('yellow', 3), ('white', 2)]

# print(counter_moscow.most_common(2))
# # [('black', 4), ('yellow', 3)]

# students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
#             ('Nikitina',2),('Markov',3),('Pavlov',2)]
# groups = dict()
 
# for student, group in students:
#     # Проверяем, есть ли уже эта группа в словаре
#     if group not in groups:
#         # Если группы ещё нет в словаре, создаём для неё пустой список
#         groups[group] = list()
#     groups[group].append(student)
 
# print(groups)
# # {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}

# from collections import defaultdict
# groups = defaultdict(list)
# for student, group in students:
#     groups[group].append(student)
 
# print(groups)
# # defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})
# print(groups[3])
# # ['Petrov', 'Markov']

# from collections import OrderedDict
# data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
# ordered_client_ages = OrderedDict(data)
# print(ordered_client_ages)
# # По результатам 3 повторов получились вот такие результаты:
# # OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# # OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# # OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])

# data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
# # Сортируем по второму значению из кортежа, то есть по возрасту
# ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
# print(ordered_client_ages)
# # OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25)])
# ordered_client_ages['Nikita'] = 18
# print(ordered_client_ages)
# # OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25), ('Nikita', 18)])

# del ordered_client_ages['Andrey']
# print(ordered_client_ages)
# # OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])
# ordered_client_ages['Andrey'] = 23
# print(ordered_client_ages)
# # OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18), ('Andrey', 23)])


# dq = deque()
# print(dq)
# # deque([])

# clients = deque()
# clients.append('Ivanov')
# clients.append('Petrov')
# clients.append('Smirnov')
# clients.append('Tikhonova')
# print(clients)
# # deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])

# first_client = clients.popleft()
# second_client = clients.popleft()
 
# print("First client:", first_client)
# print("Second client:", second_client)
# print(clients)
# # First client: Ivanov
# # Second client: Petrov
# # deque(['Smirnov', 'Tikhonova'])

# clients.appendleft('Vip-client')
 
# print(clients)
# # deque(['Vip-client', 'Smirnov', 'Tikhonova'])

# tired_client = clients.pop()
# print(tired_client, "left the queue")
# print(clients)
# # Tikhonova left the queue
# # deque(['Vip-client', 'Smirnov'])

# clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
# print(clients)
# # deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
# del clients[2]
# print(clients)
# # deque(['Ivanov', 'Petrov', 'Tikhonova'])

# # В скобках передаём список при создании deque,
# # чтобы сразу добавить все его элементы в очередь
# shop = deque([1, 2, 3, 4, 5])
# print(shop)
# # deque([1, 2, 3, 4, 5])
# shop.extend([11, 12, 13, 14, 15, 16, 17])
# print(shop)
# # deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])

# shop = deque([1, 2, 3, 4, 5])
# print(shop)
# # deque([1, 2, 3, 4, 5])
# shop.extendleft([11, 12, 13, 14, 15, 16, 17])
# print(shop)
# # deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])

# limited = deque(maxlen=3)
# print(limited)
# # deque([], maxlen=3)
 
# limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
# print(limited_from_list)
# # deque([5, 6, 7], maxlen=3)

# limited.extend([1,2,3])
# print(limited)
# # deque([1, 2, 3], maxlen=3)
 
# print(limited.append(8))
# # None
# print(limited)
# # deque([2, 3, 8], maxlen=3)


# temps = [20.6, 19.4, 19.0, 19.0, 22.1,
#         22.5, 22.8, 24.1, 25.6, 27.0,
#         27.0, 25.6, 26.8, 27.3, 22.5,
#         25.4, 24.4, 23.7, 23.6, 22.6,
#         20.4, 17.9, 17.3, 17.3, 18.1,
#         20.1, 22.2, 19.8, 21.3, 21.3,
#         21.9]
# days = deque(maxlen=7)

# for temp in temps:
#     # Добавляем температуру в очередь
#     days.append(temp)
#     # Если длина очереди оказалась равной максимальной длине очереди (7),
#     # печатаем среднюю температуру за последние 7 дней
#     if len(days) == days.maxlen:
#         print(round(sum(days) / len(days), 2), end='; ')
# # Напечатаем пустую строку, чтобы завершить действие параметра
# # end. Иначе следующая строка окажется напечатанной на предыдущей
# print("")
# # Результат:
# # 20.77; 21.27; 22.16; 23.3; 24.44; 24.94; 25.56; 26.2; 25.97;
# # 25.94; 25.57; 25.1; 24.81; 24.21; 23.23; 22.57; 21.41; 20.4;
# # 19.6; 19.1; 19.04; 18.96; 19.44; 20.01; 20.67;

# temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

# def check(temps):
#     val_temp_dict = OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))
#     return val_temp_dict
# print(check(temps))

# def check(temps):
#     temps.sort(key=lambda x: x[1], reverse=True)
#     od = OrderedDict(temps)
#     od = str(od)
#     return od
# print(check(temps))

# dq = deque([1,2,3,4,5])
# print(dq)
# # deque([1, 2, 3, 4, 5])
 
# dq.reverse()
# print(dq)
# # deque([5, 4, 3, 2, 1])

# dq = deque([1,2,3,4,5])
# print(dq)
# # deque([1, 2, 3, 4, 5])
 
# dq.rotate(2)
# print(dq)
# # deque([4, 5, 1, 2, 3])

# dq = deque([1,2,3,4,5])
# print(dq)
# # deque([1, 2, 3, 4, 5])
 
# # Отрицательное значение аргумента переносит
# # n элементов из начала в конец
# dq.rotate(-2)
# print(dq)
# # deque([3, 4, 5, 1, 2])

# dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
# print(dq.index(4))
# # 2
# print(dq.count(4))
# # 6

# dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
# print(dq.index(25))
# # ValueError: 25 is not in deque

# dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
# print(dq.count(25))
# # 0

# dq = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
# print(dq)
# # deque([1, 2, 4, 2, 3, 1, 5, 4, 4, 4, 4, 4, 3])
# dq.clear()
# print(dq)
# # deque([])

# def brackets(line):
#     if line == "": return True
#     dq = deque()
#     for elem in line:
#         if elem == '(':
#             dq.append(elem)
#         elif elem == ')':
#             if not dq: return False
#             else: dq.popleft()
#     if not dq: return True
#     else: return False
    
#     from collections import deque

# def brackets(line):
#     # Напишите тело функции
#     stack = deque()
#     for i in line:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             if len(stack) == 0:
#                 return False
#             stack.pop()
#     if len(stack) == 0:
#         return True
#     return False

# print(brackets("(()())"))
# # True
# print(brackets(""))
# # True
# print(brackets("(()()))"))
# # False

# ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
#            ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
#            ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

# # Отсортируйте список ratings по убыванию рейтинга. Для кафе с одинаковым рейтингом отсортируйте кортежи по названию.

# ratings_new = sorted(ratings, key=lambda x: (-x[1], x[0]))

# # Сохраните данные с рейтингом в словарь cafes, где ключами являются
# # названия кафе, а значениями - их рейтинг.
# from collections import OrderedDict
# cafes = OrderedDict(ratings_new)
# print(cafes)

# a=defaultdict(list)

# for x,y in ratings:
#     a[y].append(x)

# b=list(a)  
# b.sort(reverse=True)
    
# for x in a:
#     a[x]=sorted(a[x])  

# c=OrderedDict()      
# for x in b:
#     for y in a[x]:
#         c[y]=x
    
# print(dict(c))

# def task_manager(tasks):
#     target_dict = defaultdict(list)
#     dq = deque(tasks)
#     print(dq)
#     for number, server, priority in dq:
#         if priority == False:
#             target_dict[server].append(number)
#         else:
#             target_dict[server].append(number)
#     return target_dict

# def task_manager(tasks):
#     servers = defaultdict(deque)
#     for task in tasks:
#         if task[-1]:
#             servers[task[1]].appendleft(task[0])
#         else:
#             servers[task[1]].append(task[0])
#     return servers

# tasks = [(36871, 'office', False),
# (40690, 'office', False),
# (35364, 'voltage', False),
# (41667, 'voltage', True),
# (33850, 'office', False)]

# print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})

# groups = defaultdict(list)
# for student, group in students:
#     groups[group].append(student)
 
# print(groups)
# # defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})
# print(groups[3])
# # ['Petrov', 'Markov'

# a = np.int8(25)
# print(a)
# # 25

# # Можно применить к самому
# # названию типа данных
# print(np.iinfo(np.int64))
# # iinfo(min=-128, max=127, dtype=int8)

# # Можно применить к существующему
# # конкретному объекту
# print(np.iinfo(a))
# # iinfo(min=-128, max=127, dtype=int8)

# b = np.uint8(124)
# print(b)
# # 124
# print(type(b))
# # <class 'numpy.uint8'>
# print(np.iinfo(b))
# # iinfo(min=0, max=255, dtype=uint8)

# a = np.int32(1000)
# print(a)
# # 1000
# print(type(a))
# # <class 'numpy.int32'>
# a = 2056
# print(a)
# # 2056
# print(type(a))
# # <class 'int'>

# a = np.int32(1000)
# print(a)
# # 1000
# print(type(a))
# # <class 'numpy.int32'>
# a = np.int32(2056)
# print(a)
# # 2056
# print(type(a))
# # <class 'numpy.int32'>

# a = np.int32(1000)
# b = a + 25
# print(b)
# # 1025
# print(type(b))
# # <class 'numpy.int64'>

# a = np.int32(1000)
# b = np.int8(25)
# c = a + b
# print(c)
# # 1025
# print(type(c))
# # <class 'numpy.int32'>

# a = np.int8(260)
# print(a)
# # 4

# a = np.int32(2147483610)
# b = np.int32(2147483605)
# print(a, b)
# # 2147483610 2147483605
# print(a + b)
# # -81
# # RuntimeWarning: overflow encountered in int_scalars
# # Переполнено int'овое значение

# a = np.int32(2147483610)
# b = np.int32(2147483605)
# print(a, b)
# # 2147483610 2147483605
# print(np.int64(a) + np.int64(b))
# # 4294967215

# np.finfo(np.float16)
# # finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)
# np.finfo(np.float32)
# # finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)
# np.finfo(np.float64)
# # finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)


# print(np.float16(4.12))
# # 4.12
# print(np.float16(4.13))
# # 4.13
# print(np.float16(4.123))
# # 4.12
# print(np.float16(4.124))
# # 4.125
# print(np.float16(4.125))
# # 4.125

# print(np.sctypeDict)
# print(len(np.sctypeDict))
# # 158, но может быть 135 или 139

# print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

# a = True
# print(type(a))
# # <class 'bool'>
# a = np.bool(a)
# print(type(a))
# # <class 'bool'>
# a = np.bool_(a)
# print(type(a))
# # <class 'numpy.bool_'>
 
# # Значения равны
# print(np.bool(True) == np.bool_(True))
# # True
# # А типы — нет:
# print(type(np.bool(True)) == type(np.bool_(True)))
# # False

# a = "Hello world!"
# print(type(a))
# # <class 'str'>
# a = np.str(a)
# print(type(a))
# # <class 'str'>
# a = np.str_(a)
# print(type(a))
# # <class 'numpy.str_'>

# print(np.uint8(-456))

# arr = np.array([1,5,2,9,10])
# print(arr)
# # array([ 1,  5,  2,  9, 10])
# print(type(arr))
# # <class 'numpy.ndarray'>

# # Перечислить список из списков можно
# # было и в одну строку, но на нескольких
# # строках получается нагляднее
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ])
# print(nd_arr)
# # array([[12, 45, 78],
# #        [34, 56, 13],
# #        [12, 98, 76]])

# arr = np.array([1,5,2,9,10])
# print(arr.dtype)
# # dtype('int64')

# arr = np.array([1,5,2,9,10], dtype=np.int8)
# print(arr)
# # array([ 1,  5,  2,  9, 10], dtype=int8)

# arr[2] = 2000
# print(arr)
# # array([  1,   5, -48,   9,  10], dtype=int8)

# arr[2] = 125.5
# print(arr)
# # array([  1,   5, 125,   9,  10], dtype=int8)

# arr[2] = '12'
# print(arr)
# # array([ 1,  5, 12,  9, 10], dtype=int8)

# arr = np.float64(arr)
# print(arr)
# # array([ 1.,  5., 12.,  9., 10.], dtype=float128)

# arr = np.array([12321, -1234, 3435, -214, 100], dtype=np.int32)
# print(arr)
# # array([12321, -1234,  3435,  -214,   100], dtype=int32)
 
# arr = np.uint8(arr)
# print(arr)
# # array([ 33,  46, 107,  42, 100], dtype=uint8)

# arr = np.array([1,5,2,9,10], dtype=np.int8)
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ], dtype=np.int16)

# print(arr.ndim)
# # 1
# print(nd_arr.ndim)
# # 2
# print(arr.dtype)

# print(arr.size)
# # 5
# print(nd_arr.size)
# # 9
# arr.shape
# # (5,)
# nd_arr.shape
# # (3, 3)
# arr.itemsize
# # 1
# nd_arr.itemsize
# # 2

# zeros_1d = np.zeros(5)
# print(zeros_1d)
# # array([0., 0., 0., 0., 0.])

# # Создадим трёхмерный массив с формой 5x4x3 и типом float32:

# zeros_3d = np.zeros((5,4,3), dtype=np.float32)
# print(zeros_3d.shape)
# # (5, 4, 3)

# np.arange(5)
# # array([0, 1, 2, 3, 4])

# np.arange(2.5, 5)
# # array([2.5, 3.5, 4.5])

# np.arange(2.5, 5, 0.5)
# # array([2.5, 3. , 3.5, 4. , 4.5])

# np.arange(2.5, 5, 0.5, dtype=np.float16)
# # array([2.5, 3. , 3.5, 4. , 4.5], dtype=float16)

# arr = np.linspace(1, 2, 10)
# arr
# # array([1.        , 1.11111111, 1.22222222, 1.33333333, 1.44444444,
# #        1.55555556, 1.66666667, 1.77777778, 1.88888889, 2.        ])

# arr = np.linspace(1, 2, 10, endpoint=False)
# arr
# # array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])

# arr, step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
# print(step)
# # 0.1111111111111111

# arr, step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
# print(step)
# # 0.1

# arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
# print(arr)
# print(round(step, 2))

# arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
# print(arr)
# print(round(step, 2))

# arr = np.arange(8)
# arr
# # array([0, 1, 2, 3, 4, 5, 6, 7])

# arr.shape = (2, 4)
# arr
# # array([[0, 1, 2, 3],
# #        [4, 5, 6, 7]])

# arr = np.arange(8)
# arr_new = arr.reshape((2, 4))
# arr_new
# # array([[0, 1, 2, 3],
# #       [4, 5, 6, 7]])

# arr = np.arange(8)
# arr_new = arr.reshape((2, 4), order='F')
# arr_new
# # array([[0, 2, 4, 6],
# #       [1, 3, 5, 7]])

# # Будем работать с двумерным массивом:
# arr = np.arange(8)
# arr.shape = (2, 4)
# arr
# # array([[0, 1, 2, 3],
# #        [4, 5, 6, 7]])

# # Транспонируем его:
# arr_trans = arr.transpose()
# arr_trans
# # array([[0, 4],
# #        [1, 5],
# #        [2, 6],
# #        [3, 7]])

# # При транспонировании одномерного массива его форма не меняется:

# arr = np.arange(3)
# print(arr.shape)
# # (3,)
# arr_trans = arr.transpose()
# print(arr_trans.shape)
# # (3,)

# arr = np.linspace(1, 2, 6)
# arr
# # array([1. , 1.2, 1.4, 1.6, 1.8, 2. ])
# # Обратиться к его элементу по индексу можно так же, как и к списку:

# print(arr[2])
# # 1.4
# # Привычная запись для срезов работает и для одномерных массивов:

# print(arr[2:4])
# # [1.4 1.6]
# # Наконец, напечатать массив в обратном порядке можно с помощью привычной конструкции [::-1]:

# print(arr[::-1])
# # [2.  1.8 1.6 1.4 1.2 1. ]

# nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
# nd_array
# # array([[0. , 0.5, 1. , 1.5],
# #        [2. , 2.5, 3. , 3.5],
# #        [4. , 4.5, 5. , 5.5]])

# nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
# nd_array
# # array([[0. , 0.5, 1. , 1.5],
# #        [2. , 2.5, 3. , 3.5],
# #        [4. , 4.5, 5. , 5.5]])
# # Можно воспользоваться привычной записью нескольких индексов в нескольких квадратных скобках:

# nd_array[1][2]
# # 3.0

# nd_array[1, 2]
# # 3.0

# nd_array[:2, 2]
# # array([1., 3.])

# # Можно применять срезы сразу и к строкам, и к столбцам:

# nd_array[1:, 2:4]
# # array([[3. , 3.5],
# #       [5. , 5.5]])

# nd_array[:, 2:4]
# # array([[1. , 1.5],
# #       [3. , 3.5],
# #       [5. , 5.5]])

# nd_array[:2]
# # array([[0. , 0.5, 1. , 1.5],
# #       [2. , 2.5, 3. , 3.5]])

# mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
#        [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
#        [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
#        [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
#        [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
#        [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
#       dtype=np.int16)

# # В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
# elem_5_3 = mystery[4, 2]

# # В переменную last сохраните элемент из последней строки последнего столбца
# last = mystery[-1, -1]

# # В переменную line_4 сохраните строку 4
# line_4 = mystery[3]

# # В переменную col_2 сохраните предпоследний столбец
# col_2 = mystery[:, -2]

# # Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
# part = mystery[1:4, 2:5]
# print(part)

# # Сохраните в переменную rev последний столбец в обратном порядке
# rev = mystery[::-1, -1]

# # Сохраните в переменную trans транспонированный массив
# trans = mystery.transpose()

# # Способ 1. Функция np.sort(<массив>) возвращает новый отсортированный массив:

# arr = np.array([23,12,45,12,23,4,15,3])
# arr_new = np.sort(arr)
# print(arr)
# # [23 12 45 12 23  4 15  3]
# print(arr_new)
# # [ 3  4 12 12 15 23 23 45]

# # Способ 2. Функция <массив>.sort() сортирует исходный массив и возвращает None:

# arr = np.array([23,12,45,12,23,4,15,3])
# print(arr.sort())
# # None
# print(arr)
# # [ 3  4 12 12 15 23 23 45]

# data = np.array([4, 9, -4, 3])
# # Воспользуемся встроенной в NumPy функцией sqrt, чтобы посчитать квадратные корни из элементов.

# roots = np.sqrt(data)
# roots
# # RuntimeWarning: invalid value encountered in sqrt
# # array([2.        , 3.        ,        nan, 1.73205081])

# sum(roots)
# # nan

# # с помощью функции np.isnan(<массив>) узнаем, на каких местах в массиве находятся «не числа»:

# np.isnan(roots)
# # array([False, False,  True, False])

# roots[np.isnan(roots)]
# # array([nan])
# # Этим элементам можно присвоить новые значения, например 0:

# roots[np.isnan(roots)] = 0
# print(roots)
# # array([2.        , 3.        , 0.        , 1.73205081])

# sum(roots)
# # 6.732050807568877


# mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
#         -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
#         29810.], dtype=np.float32)

# # Получите булевый массив с информацией о np.nan в массиве mystery
# # True - значение пропущено, False - значение не пропущено
# nans_index = np.isnan(mystery)

# # В переменную n_nan сохраните число пропущенных значений
# n_nan = sum(nans_index)

# # Скопируйте массив `mystery` в массив `mystery_new`. Заполните пропущенные 
# # значения в массиве `mystery_new` нулями
# mystery_new = mystery.copy()
# mystery_new[nans_index] = 0

# # Поменяйте тип данных в массиве mystery на int32
# mystery_int = np.int32(mystery)

# # Отсортируйте значения в массиве по возрастанию и сохраните
# # результат в переменную array
# array = np.sort(mystery)

# # Сохраните в массив table двухмерный массив, полученный из массива array
# # В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# # по столбцам! Например, 1, 2, 3, 4 -> 1    3
# #                                      2    4
# table = array.reshape((5,3), order='F')

# #  Сохраните в переменную col столбец 2
# col = table[:, 1]


# vec1 = np.array([2, 4, 7, 2.5])
# vec2 = np.array([12, 6, 3.6, 13])
# vec1 + vec2
# # array([14. , 10. , 10.6, 15.5])

# # Что бы произошло при сложении двух списков? Их элементы просто объединились бы в один список:
# list1 = [2, 4, 7, 2.5]
# list2 = [12, 6, 3.6, 13]
# list1 + list2
# # [2, 4, 7, 2.5, 12, 6, 3.6, 13]

# # А теперь создадим vec2, который будет на один элемент короче, чем vec1:

# # vec1 = np.array([2, 4, 7, 2.5])
# # vec2 = np.array([12, 6, 3.6])
 
# # vec1 * vec2
# # ValueError: operands could not be broadcast together with shapes (4,) (3,)
# # Ошибка значения: операнд не может быть распространён одновременно на структуры с формами (4,) и (3,).

# # Исключением является случай, когда операция происходит с вектором и одним числом. 

# vec = np.arange(5)
# vec * 10
# # array([ 0, 10, 20, 30, 40])
# vec ** 2
# # array([ 0,  1,  4,  9, 16])

# vec1 = np.array([2, 4, 7, 2.5])
# vec2 = np.array([12, 6, 3.6, 13])
 
# vec1 > vec2
# # array([False, False,  True, False])

# vec = np.array([14,15,9,26,53,5,89])
# vec <= 26
# # array([ True,  True,  True,  True, False,  True, False])

# vec = np.array([3, 4])
# length = np.sqrt(np.sum(vec ** 2))
# print(length)
# # 5.0
# # Для вычисления длины вектора нам потребуется функция norm:
# length = np.linalg.norm(vec)
# print(length)
# # 5.0

# vec1 = np.array([0, 3, 5])
# vec2 = np.array([12, 4, 7])
# distance = np.sqrt(np.sum((vec1 - vec2) ** 2))
# distance
# # 12.206555615733702
# # А теперь применим более простой способ — используем уже известную нам функцию np.linalg.norm:

# vec1 = np.array([0, 3, 5])
# vec2 = np.array([12, 4, 7])
# distance = np.linalg.norm(vec1 - vec2)
# distance
# # 12.206555615733702

# vec1 = np.arange(1, 6)
# vec2 = np.linspace(10, 20, 5)
# scalar_product = np.sum(vec1 * vec2)
# scalar_product
# # 250.0


# # используют функцию np.dot(x, y):

# scalar_product = np.dot(vec1, vec2)
# scalar_product
# # 250.0

# x = np.array([25, 0])
# y = np.array([0, 10])
# np.dot(x, y)
# # 0


# # Функции np.min и np.max позволяют находить максимальное и минимальное значение в векторе. 
# vec = np.array([2,7,18,28,18,1,8,4])
# vec.min()
# # 1
# np.max(vec)
# # 28

# # Функция mean позволяет посчитать среднее значение. Больше не требуется реализовывать её «руками»!

# vec.mean()
# # 10.75

# print(np.random.rand())
# # 0.06600758835806675

# np.random.rand() * 100
# # 69.76076924077643

# np.random.rand(5)
# # array([0.83745099, 0.58426808, 0.89206204, 0.41149807, 0.42445145])

# np.random.rand(2, 3)
# # array([[0.94931212, 0.06680018, 0.26707599],
# #      [0.67908873, 0.18001743, 0.97732239]])

# np.random.rand(2, 3, 4, 10, 12, 23)

# shape = (3, 4)
# np.random.rand(shape)
# # TypeError: 'tuple' object cannot be interpreted as an integer
# # Ошибка типов: кортеж не может быть интерпретирован как целое число.

# shape = (3, 4)
# np.random.rand(*shape)
# # array([[0.66169176, 0.19455777, 0.06451088, 0.31919608],
# #        [0.73536951, 0.67104408, 0.4762727 , 0.88153576],
# #        [0.70672971, 0.96677145, 0.09273995, 0.86356465]])

# # в NumPy есть и другая функция, генерирующая массивы случайных чисел от 0 до 1, которая принимает в качестве аргумента именно кортеж без распаковки. Она называется sample:

# shape = (2, 3)
# np.random.sample(shape)
# # array([[0.39756103, 0.01995168, 0.2768951 ],
# #       [0.82195372, 0.26435273, 0.00957881]])

# # uniform(low=0.0, high=1.0, size=None)

# np.random.uniform()
# # 0.951557685543591

# np.random.uniform(-30, 50)
# # 38.47365525953661

# np.random.uniform(0.5, 0.75, size=5)
# # array([0.58078945, 0.58860342, 0.73790553, 0.63448265, 0.70920297])

# np.random.uniform(-1000, 500, size=(2, 3))
# # array([[ 129.22164163,   77.69090611, -132.9656972 ],
# #        [  18.65802226, -317.14793906,   85.3613547 ]])

# # randint(low, high=None, size=None, dtype=int)

# np.random.randint(4, size=(2,3))
# # array([[3, 0, 1],
# #       [2, 1, 3]])

# np.random.randint(6, 12, size=(3,3))
# # array([[ 9,  6, 10],
# #        [10, 11, 10],
# #        [ 7, 10, 11]])

# # Возьмём массив из целых чисел от 0 до 5 и перемешаем его:
# arr = np.arange(6)
# print(arr)
# # [0 1 2 3 4 5]
# print(np.random.shuffle(arr))
# # None
# arr
# # array([0, 5, 1, 3, 2, 4])
# # Функция random.shuffle перемешивает тот массив, к которому применяется, и возвращает None.

# playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
# shuffled = np.random.permutation(playlist)
# print(shuffled)
# # ['The Beatles' 'Pink Floyd' 'Deep Purple' 'ACDC']
# print(playlist)
# # ['The Beatles', 'Pink Floyd', 'ACDC', 'Deep Purple']

# np.random.permutation(10)
# # array([7, 8, 2, 9, 4, 3, 1, 0, 5, 6])

# # Чтобы получить случайный набор объектов из массива, используется функция random.choice:

# # choice(a, size=None, replace=True)

# workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
 
# choice = np.random.choice(workers, size=2, replace=False)
# print(choice)

# workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
# choice = np.random.choice(workers, size=10, replace=False)
# print(choice)
# # ValueError: Cannot take a larger sample than population when 'replace=False'
# # Ошибка значения: нельзя получить выборку больше, чем популяция (популяция — весь доступный набор объектов, из которого получаем выборку), если replace=False (то есть выборка без повторений).

# choice = np.random.choice([1,2,3,4,5,6], size=10)
# print(choice)
# # [3 5 5 6 6 4 2 2 1 3]

# Самостоятельно задать seed в NumPy можно с помощью функции np.random.seed(<np.uint32>). Число в скобках должно быть в пределах от 0 до 2**32 - 1 (=4294967295).

# Зададим seed и посмотрим, что получится:

# np.random.seed(23)
# print(np.random.randint(10, size=(3,4)))
# # array([[3, 6, 8, 9],
# #        [6, 8, 7, 9],
# #        [3, 6, 1, 2]])

# np.random.seed(100)
# print(np.random.randint(10, size=3))
# # [8 8 3]
# print(np.random.randint(10, size=3))
# # [7 7 0]
# print(np.random.randint(10, size=3))
# # [4 2 5]

# # Не забудьте импортировать numpy и сразу задать seed 2021
# import numpy as np
# np.random.seed(2021)
# # В simple сохранте случайное число в диапазоне от 0 до 1
# simple = np.random.rand()

# # Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# # в переменную randoms
# randoms = np.random.uniform(-150, 2021, size=120)

# # Получите массив из случайных целых чисел от 1 до 100 (включительно)
# # из 3 строк и 2 столбцов. Сохраните результат в table
# table = np.random.randint(1, 101, size=(3,2))

# # В переменную even сохраните четные числа от 2 до 16 (включительно)
# even = np.arange(2,17,2)

# # Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив mix изменился
# mix = even.copy()
# np.random.shuffle(mix)

# # Получите из even 3 числа без повторений. Сохраните их в переменную select
# select = np.random.choice(even, replace=False, size=3)

# # Получите переменную triplet, которая должна содержать перемешанные
# # значения из массива select (сам select измениться не должен)
# triplet = np.random.permutation(select)

def get_chess(a):
    square = np.zeros((a, a))
    square[1::2, ::2] = 1
    square[::2, 1::2] = 1
    return square
print(get_chess(1))
# # array([[0.]])

print(get_chess(4))
# # array([[0., 1., 0., 1.],
# #        [1., 0., 1., 0.],
# #        [0., 1., 0., 1.],
# #        [1., 0., 1., 0.]])
# arr[1::2, ::2] = 1  # [строки от индекса 1 : до конца: с шагом 2, колонки от начала  : до конца : с шагом 2 ]
# arr[::2, 1::2] = 1  # [строки  от начала  : до конца : с шагом 2 , колонки от индекса 1 : до конца: с шагом 2 ]

# def shuffle_seed(array):
#     np.random.seed()
#     ran_number = np.random.randint(1294967295)
#     shuffled = np.random.permutation(array)
#     return (shuffled, ran_number)

# def shuffle_seed(array):
#     seed = np.random.randint(2 ** 32)
#     np.random.seed(seed)
#     result = np.random.permutation(array)
#     return result, seed
# array = [1, 2, 3, 4, 5]
# print(shuffle_seed(array))
# # (array([1, 3, 2, 4, 5]), 2332342819)
# print(shuffle_seed(array))
# # (array([4, 5, 2, 3, 1]), 4155165971)

# def min_max_dist(*vectors):
#     dists = list()
#     for i in range(len(vectors)):
#         for j in range(i + 1, len(vectors)):
#             dists.append(np.linalg.norm(vectors[i] - vectors[j]))
#     return (min(dists), max(dists))
# vec1 = np.array([1,2,3])
# vec2 = np.array([4,5,6])
# vec3 = np.array([7, 8, 9])

# print(min_max_dist(vec1, vec2, vec3))
# # (5.196152422706632, 10.392304845413264)

# def any_normal(*vectors):
#     perpend = []
#     for i in range(len(vectors)):
#         for j in range(i + 1, len(vectors)):
#             perpend.append(np.dot(vectors[i], vectors[j]))
#     if 0 in perpend: return True
# vec1 = np.array([2, 1])
# vec2 = np.array([-1, 2])
# vec3 = np.array([3,4])
# print(any_normal(vec1, vec2, vec3))
# # True

# def get_loto(num):
#     loto = np.random.randint(0, 101, size=(num, 5, 5))
#     return loto
# print(get_loto(3))
# table = np.random.randint(1, 101, size=(3,2))

# def get_unique_loto(num):
#     sample = np.arange(1, 101)
#     res = list()
#     for i in range(num):
#         res.append(np.random.choice(sample, replace=False, size=(5, 5)))
#     res = np.array(res)
#     return res
# print(get_unique_loto(3))