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
        #for item in A: #Перебираем элементы входной матрцы
        for i in range(A.shape[0]):
            col=['S'+str(A.shape[0]-i-1)+'\\U'+str(A.shape[0]-i)] #Создание заголовков таблицы
            J=A[i][2]
            B=A[i][1] #Вытаскиваем итоговую матрцу
            B=[list(row) for row in B]
            for j in range(len(B)):
                print (J[j])
                B[j].append(str(J[j]))
            for row in B: # Перебор каждой строки итоговой матрицы
                col.append(str(row[0]))
            col.append('J'+str(A.shape[0]-i)+'(S'+str(A.shape[0]-i-1)+')')
            col.append('U'+str(A.shape[0]-i)+'опт')
            table_i=pt.PrettyTable()
            table_i.field_names=col
            col=[]
            for row in B:
                table_i.add_row(row) #Создание итоговой таблицы
            table.append(table_i) #Добавление итоговой таблицы в список таблиц
    return table
