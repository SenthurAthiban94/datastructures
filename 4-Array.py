from array import *

my_array = array('i',[1,2,3,4,5])

print('\nStep 1:\nIterate initalized Array')
for i in my_array:
    print(i)

print(f'\nStep 2:\naccess index of 2 {my_array[2]}')

my_array.append(6)
print(f'\nStep 3:\nAppend a value to array 6\n{my_array}')

my_array.insert(4,7)
print(f'\nStep 4:\nInsert a value 7 to array at an index 4\n{my_array}')

my_array.extend(array('i',[8,9,10]))
print(f'\nStep 5:\nExtend existing array with another array [8,9,10]\n{my_array}')

my_array.fromlist([11,12,13])
print(f'\nStep 6:\nExtend existing array with another List [11,12,13]\n{my_array}')

my_array.remove(7)
print(f'\nStep 7:\nRemove a value 7 from array\n{my_array}')

my_array.pop()
print(f'\nStep 8:\nRemove a last value from an array\n{my_array}')

print(f'\nStep 9:\nFetch element 12 from an array using index\n{my_array.index(1)}')

my_array.reverse()
print(f'\nStep 10:\nReverse an array using reverse method\n{my_array}')

print(f'\nStep 11:\nGet Array Buffer Info\n{my_array.buffer_info()}')

my_array.append(12)
print(f'\nStep 12:\nGet the number of occurences of an element 12 in an array\n{my_array}\n{my_array.count(12)}')

arr_str = my_array.tobytes()
print(f'\nStep 13:\nConvert to string\n\n{arr_str}\n')   #(tostring in older version py < 3.90)
new_arr = array('i')
print('Convert string back to array\n')
new_arr.frombytes(arr_str)
print(new_arr)

my_array.pop()
my_array.reverse()
print(f'\nStep 14:\nConvert Array {my_array} to Python List\n{my_array.tolist()}')


print(f'\nStep 15:\nSlice an Array (Start,End - 1) (2,5) in {my_array}\n{my_array[2:5]}')