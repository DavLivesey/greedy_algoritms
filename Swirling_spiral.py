import numpy as np

def swirling_spiral(count_strings, count_columns, matrix):
    matrix = np.array(matrix)
    result = []
    while (matrix.size):
        result.append(matrix[0])
        matrix = matrix[1:].T[::-1]
    return result



if __name__ == '__main__':
    count_strings = int(input())
    count_columns = int(input())
    matrix = []
    for i in range(count_strings):
        matrix.append(input().split(' '))
    print(swirling_spiral(count_strings, count_columns, matrix))