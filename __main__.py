import numpy as np
import prettytable
from modules.input_data import input_data
from modules.calculation import calculation
from modules.creating_table import creating_table


def main():
    #A = input_data()
    A=[[0,0,0,0,0],[20,7,6,14,14],[40,23,23,21,20],[60,31,30,34,35]]
    A=np.array(A)
    table = creating_table(A,0)
    B = np.array(calculation(A))
    table_result = creating_table(B,1)
    answer_file=open('answer.txt','w')
    answer_file.write('Исходные данные: \n')
    answer_file.write(str(table)+'\n')
    answer_file.write('III: \n a) \n')
    for i in range(B.shape[0]):
        answer_file.write(str(i+1)+') шаг: \n')
        answer_file.write(str(B[i][0])+'\n')
        answer_file.write(str(table_result[i])+'\n')


if __name__ == '__main__':
    main()
