import numpy as np


def calculation (A):
    result=[] #Формирование выходного списка: [[матрица B iго шага, str], ...]
    B=np.zeros((A.shape[0],A.shape[0]+2)) #Формирование второй матрицы на основе первой
    tmp = np.zeros((A.shape[0],1))
    for i in range(B.shape[0]): #Заполнение первого столбца выходной матрциы
        tmp[i][0] = A[i][0] #Формирование временного столбца
    for i in reversed(range(A.shape[1]-1)): #Решение начинается с конца; кол-во шагов равно кол-ву столбоцов F в матрице A
        if i==(A.shape[1]-2): #первая итерация отличается отпоследующих
            string = 'J'+str(i+1)+'(S'+str(i)+') = max(F'+str(i+1)+'(U'+str(i+1)+'))    0<=U'+str(i+1)+'<=S'+str(i) #формирование строки
            for j in range(A.shape[0]):
                B[j][j]=A[j][i+1] #Заполнение диагонали выходной матрицы
                B[j][-2]=np.amax(B[j], axis=0) #Заполнение столбца J(S)
                B[j][-1]=tmp[np.argmax(B[j])] #Заполнение столбца Uопт
            B=np.hstack((tmp,B))
            result.append([string,B])
        else:
            sting = 'J' +str(i+1)+'(S'+str(i)+') = max(F'+str(i+1)+'(U'+str(i+1)+'+J'+str(i+2)+'(S'+str(i-1)+'-U'+str(i)+'))    0<=U'+str(i+1)+'<=S'+str(i)
            result.append([sting,B])
    return result
