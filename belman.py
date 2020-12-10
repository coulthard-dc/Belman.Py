import numpy as np
import prettytable as pt

def input_data():
    U=list(input('Введиет бюджет U: ').split(',')) #Ввод бюджета U как строки и деление по запятой. Получение U как списка символов
    U=[int(item) for item in U] #Преобразование U в список чисел
    N=int(input('Введите количество предприятий N: ')) # Кол-во предприятий
    A=[] # Инициализируем матрицу, которая будет выступать в роли итоговой матрицы данного метода
    for i in range(N):
        tmp=list(input('Введите F'+str(i+1)+': ').split(',')) #Создание временного массива символов 
        tmp = [int(item) for item in tmp] #Преобразование массива символов в массив цифр
        A.append(tmp) #Добавление в итоговую матрицу массива F[i]
    A=np.array(A) #Преобразование списка А в матрицу A (класс модуля NumPy)
    U=np.array(U) #Преобразование массива U в массив U класса NumPy
    A=np.vstack((U,A)) #Присоединие массива U к матрице A
    A=np.transpose(A) #Транспонирование матрицы A
    return A

def draw_table(A,flag):
    if flag == 0: #Флаг нужен для определения типа таблицы (всего 2 таблицы)
        col=['Бюджет U'] #Формирование списка заголовков таблицы 
        for i in range(A.shape[1]-1):
            col.append('F'+str(i+1)) #Также формирование списка заголовков таблицы
        table0=pt.PrettyTable() #Создание объекта класса PrettyTables
        table0.field_names=col #Присвоение объекту значений заголовка таблицы
        for i in range(A.shape[0]):
            table0.add_row(A[i]) # Построчное формирование таблицы из значений матрицы A
    #else:
    return table0

    
def main():
    A=input_data()    
    #print(A)
    col=draw_table(A,0)
    table=draw_table(A,0)
    print (table)

if __name__ == '__main__':
    main()
