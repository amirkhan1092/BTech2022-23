
def size(arr):
    return len(arr), len(arr[0])

def disp_matrix(arr):
    for r in arr:
        print(*r, sep='\t')

def create_matrix(r, c, ele):
    return eval(str([[ele] * c ] * r ))     
# main code
mat1 = [[1, 2, 0], [2, 4, 4]]
mat2 = [[1, 6, 2], [3, 5, 2], [1, 3, 5]]
r1, c1 = size(mat1)
r2, c2 = size(mat2)
'''
1 X 4   4 x 4
github.com/amirkhan1092/BTech2022-23
'''
if c1 == r2:
    mat = create_matrix(r1, c2, 0)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                mat[i][j] += mat1[i][k] * mat2[k][j]             
    print('Multiplication of Two Matrix')
    print('Matrix1')
    disp_matrix(mat1)
    print('Matrix2')
    disp_matrix(mat2)
    print('Result')
    disp_matrix(mat)
else:
    print('Size is not valid for Addition')    

