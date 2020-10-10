
class Matrix:
    def __init__(self, list_1, list_2):
        self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))



my_matrix = Matrix([[6, 8, 83],
                    [26, 9, 78],
                    [4, 5, 20]],
                   [[37, 42, 0],
                    [27, 57, 62],
                    [76, 0, 0]])

print(my_matrix.__add__())