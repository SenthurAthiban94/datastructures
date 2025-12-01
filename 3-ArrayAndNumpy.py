# import numpy as np

# my_np_array = np.array([],dtype=int)
# print(my_np_array)
# my_np_int_array = np.array([1,2,3,4,5])
# print(my_np_int_array)

import array

my_array = array.array('i')                 # O(1)
print(my_array)
my_int_array = array.array('i',[1,2,3,4,5])  # O(N)
print(my_int_array)
my_int_array.insert(100,6)          # O(N) index, value higher the index out of bound inserts into last element
print(my_int_array)

def traversal(arr):
    for i in arr:
        print(i)
    print('\n')

def access_element(arr,index):
    if index >= len(arr):           # O(1)
        print(f'No element in index {index}')
    else:
        print(arr[index])

def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return print(i)
    return print(-1)

def remove_element(arr,val):
    arr.remove(val)
    print(arr)

traversal(my_int_array)         # O(N)
access_element(my_int_array,5)  # O(1)
remove_element(my_int_array,4)  # O(N)
linear_search(my_int_array,4)   # O(N)





