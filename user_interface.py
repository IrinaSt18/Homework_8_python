from logger import *

def interface():
    print("""1 - добавить данные,
          2 - найти данные,
          3 - вывести на экранб
          4 - импорт в файл,
          5 - удалить запись,
          6 - внести изменения в запись""")
    var = int(input("введите номер варианта: "))
    # while var not in ("1", "2", "3", "4", "5", "6"):
    #     print("Вариант не верный")
    #     var = input("Введите номер варианта: ")
    if var == 1:
        input_data()
    elif var == 2:
        search()
    elif var == 3:
        print_data()
    elif var == 4:
        load()
    elif var == 5:
        delete_str()
    elif var == 6:
        change_str()
    else:
        print("Такой команды не существует: ")
        