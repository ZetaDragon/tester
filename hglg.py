#my map
'''  def my_map(function,list_el):
    new_list=[]
    for iterable in list_el:
        new_list.append(function(iterable))
    return new_list

list_el = [1,2,3,4,5,6,7,8,9,10]
print(my_map(lambda element: element*2, list_el))
'''
'''list_el = [1,2,3,4,5,6,7,8,9,1]
print(list(filter(lambda  element: element%2==0,list_el)))'''

'''
from pickle import dump, load
car = 'tesla'
year = 2016
with open('test.doc','wb') as fileHandler:
    dump(car,fileHandler)
    dump(year,fileHandler)

with open('test.doc', 'rb') as fileHandler:

    year = load(fileHandler)
    print(year)
'''

'''from pickle import dump,load

doc_file = r'.doc'

car = ['BMW','Rolls-Royce','Porshe', 'Bugatti']
cars_info = [['BMW','m5',2022,2.8],
             ['Rolls-Royce','GHOST',2020,4.5],
             ['Porshe','Taycan',2019,2,7],
             ['Bugatti','Chiron',2018,2.1]]

with open(doc_file, 'wb') as fileHandler:
    for i in cars_info:
        dump(i,fileHandler)

with open(doc_file, 'rb') as fileHandler:
    for i in range(len(cars_info)-1):
        x = load(fileHandler)
        print(x)
        for j in range(len(cars_info[i])):
            print(f'position number = {j} has element with value = {x[j]}')'''


#task1
#1. Поиск и замена слов списка в содержимом бинарного файла
#2. Подсчет количества слов и чисел(по отдельности) в содержимом бинарного файла
#3. Вывести слова спрятанные за ключами в словае в содержимом бинарном файле
#task1
'''list_el = ['ceburek' , 'arbuz', 'vishnya']
with open('file.doc','wb') as fileHandler:
    contend = fileHandler.read()
for i in list_el'''
def find_and_delete(list,search,zamena):
    with open(doc_file,"wb") as file:
        for i in list:
            dump(i,file)
    with open(doc_file,"rb") as fileHandler:
        считать с цикла элементы
        a = load(fileHandler)
