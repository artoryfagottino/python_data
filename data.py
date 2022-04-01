
def show(file_format):# если формат равен 1 ,тогда 
    if file_format == 1:
        return open("user.scv","r",encoding="utf - 8")# тогда просто возвращаем данные из указаного файла user.scv
    else:
        return open("user_sec.scv","r",encoding="utf - 8")# Если формат равен 2,тогда данные из указанного файла user_sec.scv
    
def write(file_format,user_data):# сюда приходят данные из main  
    if file_format == 1:
        data = open("user.scv","a",encoding= "utf - 8")# если формат 1 файла,то будет первый формат и дозаписываем
        data.write("\n")#добавляем путсую строку 
        for i in range(0,len(user_data)):# и циклом добавляем каждый элемент этого списка 
            data.write(f"\n{user_data[i].replace(' ','')}")# с новой строки и убирая лишние пробелы 
    else:
        data = open("user_sec.scv","a",encoding="utf - 8")#если формат файла 2 то мы просто открывам 2 фаил 
        data.write(f"\n{user_data[0].replace(' ','')}")# записывя с новой стоки удаляя лишние пробелы 
        for i in range(1, len(user_data)):# циклом пробегаемся от 1 элемента до последнего 
            data.write(f",{user_data[i].replace(' ','')}")# добавляем с , и пробелом и так же удаляя лишние пробелы 
        data.write(";")# и в конце добавялем ;