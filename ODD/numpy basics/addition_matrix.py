# matrix addition
import numpy as np
# m1 = [[3, 5, 2], [2, 5, 3], [1, 4, 6]]
# m2 = [[1, 2, 3], [1, 1, 1], [0, 0, 0]]
# r1, c1 = map(int, input('Enter the shape of first Matrix RxC').split('x'))
r1 = int(input('Enter the row of first Matrix '))
c1 = int(input('Enter the column of first Matrix '))
m1 = eval(str([[0] * c1]* r1))
for i in range(r1):
    for j in range(c1):
        m1[i][j]= int(input(f'Enter the element {i+1}x{j+1}'))

r2 = int(input('Enter the row of Second Matrix '))
c2 = int(input('Enter the column of Second Matrix '))
m2 = eval(str([[0] * c2]* r2))
for i in range(r2):
    for j in range(c2):
        m2[i][j]= int(input(f'Enter the element {i+1}x{j+1}'))

arr1 = np.array(m1)
arr2 = np.array(m2)

# logic section
if arr1.shape[1] == arr2.shape[0]:
    out = np.dot(arr1, arr2)
    print('Matrix1')
    print(arr1)
    print('Matrix2')
    print(arr2)
    print('Multiplication')
    print(out)
else:
    print('Shape is not valid for Matrix Multiplication')