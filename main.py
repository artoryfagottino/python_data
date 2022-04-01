
import view 
import data as file_data

while not (view.action == 1 or view.action == 2 ):#проверка пока action не будет равна 1 или 2(ввод или вывод справочника/действие )
    view.error()# если выше не выполняется условие вывод ошибки показывать 

if view.action == 1:#если ввод равен 1 ,тогда в ввод записываем 
    data = file_data.show(view.file_format)# записываем в file_data и запускаем метод show из файда data.py/в который отправляем ввид формата 1 или 2
    view.show_users(data.read())# отправляем во view show_users(в функцию которая просто выводит) эту самую дату data.read.
    data.close()# после выполнения ее закрывает 
else:
    user_data = view.add_user().split(" , ")# иначе если 2 действие ровно вводу,то в значение user_data добавляем функцию из (файла view.py)view.add_user()
    #которая работает с пользователем,получает строку,разделенную запятой,превращет ее как бы в список 
    file_data.write(view.file_format,user_data)# и дальше user_data отправляет в файл data в метод def write с аргументами file_format,user_data

