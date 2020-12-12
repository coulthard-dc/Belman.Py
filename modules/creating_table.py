import numpy as np
import prettytable as pt


def creating_table(A,flag):
    if flag == 0: #Флаг нужен для определения типа таблицы (всего 2 таблицы)
        col=['Бюджет U'] #Формирование списка заголовков таблицы 
        for i in range(A.shape[1]-1):
            col.append('F'+str(i+1)) #Также формирование списка заголовков таблицы
        table=pt.PrettyTable() #Создание объекта класса PrettyTables
        table.field_names=col #Присвоение объекту значений заголовка таблицы
        for i in range(A.shape[0]):
            table.add_row(A[i]) # Построчное формирование таблицы из значений матрицы A
    else:
        table=[]; #Формирорование выхожного списка таблиц
        for item in A: #Перебираем элементы входной матрцы
            col=['U\\S'] #Создание заголовков таблицы
            J=item[2]
            B=item[1] #Вытаскиваем итоговую матрцу
            B=[list(row) for row in B]
            for i in range(len(B)):
                print (J[i])
                B[i].append(str(J[i]))
            for row in B: # Перебор каждой строки итоговой матрицы
                col.append(str(row[0]))
            col.append('J(S)')
            col.append('Uo')
            table_i=pt.PrettyTable()
            table_i.field_names=col
            for row in B:
                table_i.add_row(row) #Создание итоговой таблицы
            table.append(table_i) #Добавление итоговой таблицы в список таблиц
    return table
