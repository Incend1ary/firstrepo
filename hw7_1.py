class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(itm) for itm in line) for line in self.matrix)


    def __add__(self, other):
        c = []
        for line in range(len(self.matrix)):
            c.append([])
            for itm in range(len(self.matrix[line])):
                c[line].append(self.matrix[line][itm] + other.matrix[line][itm])
        return Matrix(c)


matrix_1 = Matrix([[1, 2], [2, 3], [3, 5]])
matrix_2 = Matrix([[2, 5], [5, 9], [1, 7]])
print(matrix_1, end="\n \n")
print(matrix_2, end="\n \n")
print(matrix_1 + matrix_2)