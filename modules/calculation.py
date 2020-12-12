import numpy as np


def calculation (A):
    result=[] #Формирование выходного списка: [[матрица B iго шага, str], ...]
    B=np.zeros((A.shape[0],A.shape[0]+1)) #Формирование второй матрицы на основе первой
    tmp = np.zeros((A.shape[0],1))
    for i in range(B.shape[0]): #Заполнение первого столбца выходной матрциы
        tmp[i][0] = A[i][0] #Формирование временного столбца
    for i in reversed(range(A.shape[1]-1)): #Решение начинается с конца; кол-во шагов равно кол-ву столбоцов F в матрице A
        cell=[]
        if i==(A.shape[1]-2): #первая итерация отличается отпоследующих
            string = 'J'+str(i+1)+'(S'+str(i)+') = max(F'+str(i+1)+'(U'+str(i+1)+'))    0<=U'+str(i+1)+'<=S'+str(i) #формирование строки
            for j in range(B.shape[0]):
                B[j][j]=A[j][i+1] #Заполнение диагонали выходной матрицы
                B[j][-1]=np.amax(B[j], axis=0) #Заполнение столбца J(S)
                cell_tmp=[] #ЗАПОЛНЕНИЕ СТОЛБЦА Uоптимальное
                cell_tmp.append(int(tmp[np.argmax(B[j])]))
                cell.append((cell_tmp))
                cell_tmp=[]
            B=np.hstack((tmp,B))
            result.append([string,B,cell])
        else:
            B=np.zeros((A.shape[0],A.shape[0]+1))
            for j in range(B.shape[0]):
                for k in range (j+1):
                    tmp_B=result[-1][1]
                    B[j][k] = A[k][i+1]
                    J_value=tmp[j][0]-tmp[k][0]
                    index = list(np.transpose(tmp)[0]).index(J_value)
                    B[j][k]+=tmp_B[index][-1]
                B[j][-1]=np.amax(B[j], axis=0) #Заполнение столбца J(S)

                cell_tmp = []
                for k in range (j+1):
                    if B[j][k] == np.amax(B[j], axis = 0):
                        cell_tmp.append(int(tmp[k][0]))
                cell.append((cell_tmp))
                cell_tmp=[]
            B=np.hstack((tmp,B))
            sting = 'J' +str(i+1)+'(S'+str(i)+') = max(F'+str(i+1)+'(U'+str(i+1)+'+J'+str(i+2)+'(S'+str(i-1)+'-U'+str(i)+'))    0<=U'+str(i+1)+'<=S'+str(i)
            result.append([sting,B,cell])
    return result
