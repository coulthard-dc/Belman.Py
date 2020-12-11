import numpy as np
import prettytable
from modules.input_data import input_data
from modules.calculation import calculation
from modules.creating_table import creating_table


def main():
    A = input_data()
    table = creating_table(A,0)
    B = np.array(calculation(A))
    table_result = creating_table(B,1)
    print(table)
    for i in range(B.shape[0]):
        print(B[i][0])
        print(table_result[i])


if __name__ == '__main__':
    main()
