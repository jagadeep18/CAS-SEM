# Transpose of a matrix
list1 = [[1,2,3],[4,5,6],[7,8,9]]
transpose = list(map(list,zip(*list1)))
print(transpose)

transpose1 = [[list1[i][j] for j in range(len(list1))] for i in range(len(list1[0]))]
print(transpose1)