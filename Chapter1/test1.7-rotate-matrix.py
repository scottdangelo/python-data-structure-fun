#! /usr/bin/env python

matrix1 = [[(1,1,0,0), (0,1,0,1), (1,1,1,0)],
           [(0,0,1,0), (1,0,0,1), (0,0,0,0)],
           [(1,1,1,1), (0,1,1,1), (0,1,0,0)]]
test1 = matrix1[0][1]
out_matrix = matrix1

for i, r in enumerate(matrix1):
    for j, c in enumerate(matrix1[i]):
        out_matrix[j][i] = matrix1[i][j]

print(matrix1)
print(out_matrix)