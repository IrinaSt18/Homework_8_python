from data_create import *

def input_data():
    name = name_data()
    lastname = lastname_data()
    phone = phone_data()
    address = address_data()
    # var = input(f"""В каком формате записать данные? 
    #             1 вариант:
    #             {lastname},
    #             {name},
    #             {phone},
    #             {address}
    #             2 вариант:
    #             {lastname};{name};{phone};{address}
    #             Введите номер варианта: """)
    # while var not in ("1", "2"):
    #     print("Вариант не верный")
    #     var = input("Введите номер варианта: ")
    # if var == "1":
    #     with open("data_first.txt","a", encoding = "utf-8") as file:
    #         file.write(f"{name}\n{lastname}\n{phonenum}\n{address}\n\n")
    # else:
    #     with open("data_first.txt","a", encoding = "utf-8") as file:
    #         file.write(f"{name};{lastname};{phonenum};{address}\n\n")
    with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt","a", encoding = "utf-8") as file:
        file.write("\n")
        file.write(f"{lastname}\t{name}\t{phone}\t{address}")

def print_data():
    with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt","r", encoding = "utf-8") as data:
        data_first = data.read()
        # data_first = data.readlines()
        # print(data_first)
        # temp = []
        # j = 0
        # for i in range(len(data_first)):
        #   if data_first[i] == "\n" or i==len(data_first)-1:
        #       temp.append("".join(data_first[j:i+1]))
        #       j=i
        # data_first = temp
        # print(data_first)
        print(data_first)
    return data_first 

def search():
    search1 = input("Введите данные для поиска: ")
    inform = False
    with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt","r",encoding = "utf-8")as data:
        for line in data:
            if search1 in line:
                print(line)
                inform = True
        if inform == False:
            print("Данные не найдены")

def load():
    new_inform = input("Укажите файл для импорта")
    with open(new_inform, "r", encoding="utf-8") as data:
        with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt", "a+", encoding = "utf-8") as data1:
            data1.write("\n")
            for line in data:
                if line not in data1:
                    data1.write(line)

def delete_str():
    str_for_delete = input("Введите данные, которые нужно удалить: ")
    with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt", "r", encoding = "utf-8") as data:
        info = data.readlines()
        with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt", "w", encoding = "utf-8") as data1:
            for line in info:
                if str_for_delete not in line:
                    data1.write(line)
                    
def change_str():
    line_for_change = input("Введите данные, которые нужно изменить: ") 
    with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt", "r", encoding = "utf-8") as data:
        inform = data.readlines()
        with open("C:\Users\user\Desktop\Learning\Python\Homework\Homework_8\Task_38\data_first.txt", "w", encoding = "utf-8") as data1:
            for line in inform:
                if line_for_change not in line:
                    data1.write(line)
                else:
                    print(line)   
                    ask = input("Удалить эту строку (y,n)? ")
                    if ask == "n":
                        data1.write(line)
                        
        
    
            