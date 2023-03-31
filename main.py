'''def fileWork(file,fileMode,info = None):
    fileHandler = open(file,fileMode)
    if fileMode == "w":
        fileHandler.write(info)
    elif fileMode =="r":
        print(fileHandler.read())
    elif fileMode == "a":
        fileHandler.write(info)
    else:
        return -1
    fileHandler.close()

fileName = input('Write file name: ')
while True:
    choice = int(input("what do you want to do with file:\n1.Rewrite info\n2.Print info.\n3.Add info\n"))
    if choice==1:
        info = input("Rewrite info from file to:\n")
        fileWork(fileName,"w",info)
    elif choice==2:
        fileWork(fileName,"r")
    elif choice == 3:
        info = input("Rewrite info from file to:\n")
        fileWork(fileName,"a",info)
    else:
        break'''

'''
try:
    fileHandler = open(r'C, 'r')
    try:
        fileHandler.write('')
    except Exception as e :
        print(f"Program interrupted by the error: {e}")
    finally:
        fileHandler.close()
except Exception as ex:
    print(f"Program interrupted by the error: {ex}")'''

#with open(r'C:\Users\Sadyg_pt58\PycharmProjects\pythonProject','r',encoding='UTF8') as fileHandler:
# print(fileHandler.read())

#my_file_path = r'C:\Users\Sadyg_pt58\PycharmProjects\pythonProject.txt'
'''list_string = list()

for i in range(4):
    str = input('add line info:\n')
    list_string.append(str)
    
with open(my_file_path,'a') as file:
        for i in list_string:
            file.write(i)
    

with open(my_file_path,'r') as file :
    print(file.read())'''

