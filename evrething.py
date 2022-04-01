# main
# import view 
# import data as file_data

# while not (view.action == 1 or view.action == 2 ):#проверка пока action не будет равна 1 или 2(ввод или вывод справочника/действие )
#     view.error()# если выше не выполняется условие вывод ошибки показывать 

# if view.action == 1:#если ввод равен 1 ,тогда в ввод записываем 
#     data = file_data.show(view.file_format)# записываем в file_data и запускаем метод show из файда data.py/в который отправляем ввид формата 1 или 2
#     view.show_users(data.read())# отправляем во view show_users(в функцию которая просто выводит) эту самую дату data.read.
#     data.close()# после выполнения ее закрывает 
# else:
#     user_data = view.add_user().split(" , ")# иначе если 2 действие ровно вводу,то в значение user_data добавляем функцию из (файла view.py)view.add_user()
#     #которая работает с пользователем,получает строку,разделенную запятой,превращет ее как бы в список 
#     file_data.write(view.file_format,user_data)# и дальше user_data отправляет в файл data в метод def write с аргументами file_format,user_data

#data 
# def show(file_format):# если формат равен 1 ,тогда 
#     if file_format == 1:
#         return open("user.scv","r",encoding='utf - 8')# тогда просто возвращаем данные из указаного файла user.scv
#     else:
#         return open("user_sec.scv","r",encoding='utf - 8')# Если формат равен 2,тогда данные из указанного файла user_sec.scv
    
# def write(file_format,user_data):# сюда приходят данные из main  
#     if file_format == 1:
#         data = open("user.scv","a",encoding='utf - 8')# если формат 1 файла,то будет первый формат и дозаписываем
#         data.write('\n')#добавляем путсую строку 
#         for i in range(0,len(user_data)):# и циклом добавляем каждый элемент этого списка 
#             data.write(f"\n{user_data[i].replase(' ','')}")# с новой строки и убирая лишние пробелы 
#     else:
#         data = open("user_sec.scv","a",encoding='utf - 8')#если формат файла 2 то мы просто открывам 2 фаил 
#         data.write(f"\n{user_data[0].replase(' ','')}")# записывя с новой стоки удаляя лишние пробелы 
#         for i in range(1, len(user_data)):# циклом пробегаемся от 1 элемента до последнего 
#             data.write(f",{user_data[i].replace(' ','')}")# добавляем с , и пробелом и так же удаляя лишние пробелы 
#         data.write(";")# и в конце добавялем ;
# view 
# def error():# Функция ошибки,если формат файла(1 или 2)введене не верно 
#     print('Введенное значение должно равняться 1 или 2 ')
#     global action 
#     action = int(input())

# def show_users(data):#Эта функция просто выводит справочник 
#     print(data)

# def add_user():# Добавляет значение нового пользователя в мини (базу данных)
#     print("Введите данные пользователя в формате 'Фамилия, Имя, Телефон , описание ")
#     return input()

# action = int(input("Справочник\nВыберите действие:\n1. Показать контакты\n2. Добавить контакты\n"))
# # action - получаем данные для справочника 
# file_format = int(input("Выберите формат файла:\n1./Фамилия/Имя/Телефон/описание\n2.Фамилия,Имя,Телефон,описание\n"))
# #file_format - тут записывается 1 или 2 в каком формате записывать данные/вывод либо ввод 