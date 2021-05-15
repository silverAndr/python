class Matrix:
    def __init__(self, matrix_list):
        if isinstance(matrix_list, list):
            for matrix_row in matrix_list:
                if not isinstance(matrix_list, list):
                    return 'Error'
        else:
            return 'Error'
        self.matrix_list = matrix_list

    def __str__(self):
        for matrix_row in self.matrix_list:
            for i in matrix_row:
                print(i, end=' ')
            print('')
        return ''

    def __add__(self, other):
        result_list = []
        for row_num, matrix_row in enumerate(self.matrix_list):
            new_row = []
            for i, num in enumerate(matrix_row):
                new_row.append(num + other.matrix_list[row_num][i])
            result_list.append(new_row)
        # print(result_list)
        return Matrix(result_list)



matrix1 = [[1, 2, 3, 4], [5, 4, 3, 2], [4, 6, 7, 9]]
matrix2 = [[1, 2, -3, -4], [5, -4, -3, 2], [2, 3, 1, 0]]

new_matrix1 = Matrix(matrix1)
new_matrix2 = Matrix(matrix2)
print(new_matrix1 + new_matrix2)
