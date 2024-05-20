import csv
import os
os.system('cls')
file_patches = []
candidates = []
sorted_data = []
unsorted_data = []
approved_canditades = []
result_candidates = []
NEEDED_ROW_SEQUNCE = {'id': 0,
        'name': 1,
        'surname': 2,
        'age': 3,
        'height': 4,
        'weight': 5,
        'eyesight': 6,
        'education': 7,
        'english_language': 8,
        }


def GetRowsNumber(thefile): # возвращает количество строк в файле csv 
    with open(thefile) as file:
        return len(list(csv.reader(file)))
    
def GetFilePatches(): # получение путей от ввода пользователя
    global file_patches
    while True:
        os.system("cls")
        print("="*70)
        print('введите пути таблиц, каждый новый путь отделяйте нажатием клавиши ENTER, для начала обработки данных введите: старт')
        print("пример: D:\рабочий стол\CSVshki\ger.csv")
        print("="*70)
        print("выбранные пути:",file_patches)
        file_path = input("введите путь:")
        if file_path != "старт":
            file_patches.append(file_path)
        else:
            os.system('cls')
            break
            
def GetAllData(path): # получение данных для фильтрации
    global unsorted_data
    unsorted_data = []
    with open(path,) as f:
        print("="*70)
        print(path, ":открыт")
        reader = csv.reader(f, delimiter ='#')
        for i in range(GetRowsNumber(path)):
            reader = csv.reader(f, delimiter='#')
            unsorted_data.append(next(reader))
    unsorted_data.pop(0)
    SortRows(path)
    
def SortRows(path):
    with open(path,) as f:
        reader = csv.reader(f, delimiter ='#')
        keylist = next(reader)
        sorting_order_list = []
        for key in keylist: # создание порядка для сортировки
            sorting_order_list.append(NEEDED_ROW_SEQUNCE[key])
    for candidate in unsorted_data:
        temp_S = {}
        temp_D = {}
        for i in range(0,9):
            temp_D[candidate[i]] = sorting_order_list[i]
        for human,index in temp_D.items():
            temp_S[index] = human  
        sorted_data.append(temp_S)
    print("сортировка файла прошла успешно")   
                  
def DeleteInappropriate(): # удаление неподходящих кандидатов
    for candidate in sorted_data:
        if 20 <= int(candidate[3]) or int(candidate[3]) >= 59:
            if 150 <= int(candidate[4]) and int(candidate[4]) <= 190:
                if float(candidate[6]) == 1.0:
                    if candidate[7] == 'Master' or candidate[7] == 'PhD':
                        if candidate[8] == 'true':
                            approved_canditades.append(candidate)                   
    print("="*70)
    print("фильтрация прошла успешно")
    
def SortApproved(): # cортировка отобранных
    in_priority = []
    not_a_priority = []
    for candidate in approved_canditades:
        if int(candidate[3]) >= 27 and int(candidate[3]) <= 37:
            in_priority.append(candidate)
        else:
            not_a_priority.append(candidate)
        in_priority = sorted(in_priority, key=lambda i: (i[1], i[2]))
        not_a_priority = sorted(not_a_priority, key=lambda i: (i[1], i[2]))
        result_candidates = in_priority + not_a_priority
    for id, candidate in enumerate(result_candidates, start=1):
        candidate[0] = id
    print("="*70)
    print("сортировка кандидатов прошла успешно")
    CreateResultFile(result_candidates)    
    
def CreateResultFile(data):
    with open('result.csv', 'w+', newline='') as file:
        writer = csv.writer(file, delimiter='#')
        for element in data:
            writer.writerow([element[0],
                             element[1],
                             element[2],
                             element[4],
                             element[5],
                             element[7],
                             ])
    print("="*70)
    print('создание файла "result" прошло успешно')
    
GetFilePatches()
for path in file_patches:
    GetAllData(path)  
DeleteInappropriate()
SortApproved()
