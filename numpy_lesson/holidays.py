# import pandas as pd
# def get_street_type(address):
# # Создаём список географических пометок exclude_list.
#     exclude_list = ['N', 'S', 'W', 'E']
# # Метод split() разбивает строку на слова по пробелу.
# # В результате получаем список слов в строке и заносим его в переменную address_list.
#     address_list = address.split(' ')
# # Обрезаем список, оставляя в нём только последний элемент,
# # потенциальный подтип улицы, и заносим в переменную street_type.
#     street_type = address_list[-1]
# # Делаем проверку на то, что полученный подтип является географической пометкой.
# # Для этого проверяем его на наличие в списке exclude_list.
#     if street_type in exclude_list:
# # Если переменная street_type является географической пометкой,
# # переопределяем её на второй элемент с конца списка address_list.
#         street_type = address_list[-2]
# # Возвращаем переменную street_type, в которой хранится подтип улицы.
#     return street_type
# print(get_street_type('2/119 Railway St N'))

# def correct_type(street_type):
#     dict = {'Avenue':'Av', 'Boulevard':'Bvd', 'Parade':'Pde'}
#     if street_type in dict.keys():
#         return dict.get(street_type)
#     else:
#         return street_type  
# print(correct_type('Avenue'))

import pandas as pd
import os

def concat_users_files(path):
    file_name = os.listdir(path)
    file_name = sorted(file_name)
    print ('Файлы в папке:',file_name)
    for i in range(len(file_name)-1):
        if i == 0 :
            df_dates = pd.read_csv(path+'/'+file_name[i])
        else: 
            date = pd.read_csv(path+'/'+file_name[i])
            df_dates = pd.concat([df_dates,date],ignore_index=True)
    df_dates = df_dates.drop_duplicates(ignore_index=True)    
    return df_dates

data = concat_users_files(r'C:\Users\ceasa\IDE\test 2\project_1\Skillfactory\Pandas\PY12\user')
data