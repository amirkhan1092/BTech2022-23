# addition of two matrix 
def valid_matrix(arr):
    ln = len(arr[0])
    for r in arr:
        if ln != len(r):
            return False
    return True    
def dimension(arr):
    return len(arr), len(arr[0])  

def create_matrix(r, c, ele):
    return eval(str([[ele] * c ] * r ))
# main code 
mat1 = [[3, 5, 1], [2, 4, 6]]
mat2 = [[4, 6, 2], [2, 5, 8]]

if valid_matrix(mat1) and valid_matrix(mat2):
    # validity for addition
    r1, c1 = dimension(mat1)
    r2, c2 = dimension(mat2) 
    if (r1, c1) == (r2 ,c2):
        mat = create_matrix(r1, c1, 0)


        mat1[0][0]  + mat2[0][0]
    else:
        print('Dimension not match for Addition')
else:
    print('Invalid Matrix')