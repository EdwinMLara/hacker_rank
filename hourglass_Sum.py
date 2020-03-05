import numpy as np

def hourglassSum(arr):
    mask = [[1,1,1],[0,1,0],[1,1,1]]
    result_mask = [[0,0,0],[0,0,0],[0,0,0]]
    
    aux_result = 0
      
    for i in range(1,5):
        for k in range(1,5):
            submatrix = arr[i-1:i+2,k-1:k+2]
            result = 0

            for i1 in range(3):
                for k1 in range(3):
                    result_mask[i1][k1] = submatrix[i1][k1] * mask[i1][k1]
                    result += result_mask[i1][k1]
                    
            if(aux_result < result):
                aux_result = result
    
    return aux_result

arr = np.array([[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]])

arr2 = np.array([[1, 1, 1, 0, 0, 0,],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 9, 2, -4, -4, 0],
[0, 0, 0, -2, 0, 0], 
[0, 0, -1, -2, -4, 0]])

arr3 = np.array([[-9, -9, -9, 1, 1, 1],
[0, -9, 0, 4, 3, 2],
[-9, -9, -9, 1, 2, 3],
[0, 0, 8, 6, 6, 0],
[0, 0, 0, -2, 0, 0],
[0, 0, 1, 2, 4, 0]])
print(hourglassSum(arr))