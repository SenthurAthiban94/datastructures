import numpy as np

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

# O(MN)
two_dimensional_arr = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])                                              

print(two_dimensional_arr)

# Inserting into 2 dimensional Array
columnAddition = np.insert(two_dimensional_arr,0,[[1,2,3,4]],axis=1)
rowAddition = np.insert(two_dimensional_arr,0,[[1,2,3,4]],axis=0)
print(f'After inserting Column\n{columnAddition}')
print(f'After inserting Row\n{rowAddition}')

# Index not required in append
print(two_dimensional_arr.shape)
# columnappend = np.append(two_dimensional_arr,[[1,2,3,4]],axis=1)
rowappend = np.append(two_dimensional_arr,[[1,2,3,4]],axis=0)
colappend = np.append(two_dimensional_arr,[[1],[2],[3],[4]],axis=1)
print(f'After Appending Row\n{rowappend}')
print(f'After Appending Column\n{colappend}')


def access_elements(arr,ri,ci):                             # O(1)
    if ri>=len(arr) and ci<=len(arr[0]):
        print('No element exist in this index')
    else:
        print(arr[ri][ci])

def traverse_arr(arr):
    print(f'\nTraversing through array\n{arr}\n')
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(f'({i},{j}) => {arr[i][j]}')

def linear_search(arr,val):
    print(f'\nFinding {val} using linear search from \n{arr}')
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == val:
                return print(f'({i},{j}) => {val}')
    return print('-1')

def delete_row(arr, rowIndex):
    print(f'\n Before Deleting row\n {arr}')
    newArray = np.delete(arr,rowIndex,axis=0)
    print(f'\n After Deleting row\n {newArray}')
    
def delete_col(arr, colIndex):
    print(f'\n Before Deleting column\n {arr}')
    newArray = np.delete(arr,colIndex,axis=1)
    print(f'\n After Deleting column\n {newArray}')

print(f'Accessing element(0,1) from \n{two_dimensional_arr}')
access_elements(two_dimensional_arr,0,1)                    # O(1)
delete_row(two_dimensional_arr,0)                           # O(MN)
delete_col(two_dimensional_arr,0)                           # O(MN)
traverse_arr(two_dimensional_arr)                           # O(MN)
linear_search(two_dimensional_arr,12)                       # O(MN)