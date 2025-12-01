# Empty list
emptylist = []
print(emptylist)

# Integer List
integers = [1,2,3,4,5]
print(integers)

# String List
strings = ['this','is','a','string','list']
print(strings)

# Mixed datatype List
mixedList = [1,'senthur',True]
print(mixedList)

# Nested List
nestedList = ['hello',1,['world',2]]
print(nestedList)

# Accessing List
newList = ['senthur', 'athiban']
print(newList[0],newList[1])
print(f'\nCheck if senthur exist in list {newList}\n{'senthur' in newList}')

# Find last Element in list
print(f'Accessing last element from the list {newList} by newList[-1]\n{newList[-1]}')

# Traversing through the list
print(f'Traversing through the list {newList}')
for i in range(len(newList)):
    newList[i]+='+'
    print(newList[i])

# Traversing through the empty list
for i in range(len(emptylist)):
    print("It won't reach here as it is an empty list")
print('\n')


# Inserting into List
    # Insert in beginning
    # Insert in end
    # Insert into particular index
    # Insert another list into this list

listItems = [1,2,3,4,5]
print(f'After inserting 0 in 0th index of list {listItems}')
listItems.insert(0,0)
print(f'{listItems} -> O(N)')
print(f'After appending 6 into the list {listItems}')
listItems.append(6)
print(f'{listItems} -> O(1)')
updatedList = [7,8,9,10]
print(f'O(N) After extending list {listItems} with list {updatedList}')
listItems.extend(updatedList)
print(f'{listItems} -> O(N)\n')

# Slicing List
sliceList = ['a','b','c','d','e']
print(f'Slicing list {sliceList} including start(0) and excluding end(3) [0:3]\n{sliceList[0:3]}')
print(f'Updating list with items a->x and b->y using slice in {sliceList}')
sliceList[0:2] = ['x','y']
print(sliceList)

# Delete an Item from list
sliceList.remove('x')
print(f'Remove an item from list using the value by remove method\n{sliceList} -> O(N)')
del sliceList[0]
print(f'Delete an item from list using the delete method\n{sliceList} -> O(N)')
sliceList.pop()
print(f'Remove the last element of list using pop method\n{sliceList} -> O(1)')

sliceList.insert(0,'b')
# Searching an element in list
target = 'd'
print(f'\nSearching an element ({target}) in list {sliceList}')
if target in sliceList:
    print(f'Element {target} exist!')
else:
    print(f'Element {target} does not exist!')

def linear_search(list,target):
    for i in range(len(list)):
        if target==list[i]:
            return i
    return -1

print(f'Searching for {target} in list {sliceList}\n{linear_search(sliceList,target)} --> O(N)')

# List Operators
# + operator - Concatination
a = [1,2,3]
b = [4,5,6]
c = a+b
print(f'\nConcatinating {a} and {b}\n{c}')

# * operator - Repeats the elements 
a = [1,2]
c = a*2
print(f'\n* Operator on {a}\n{c}')

# len function - find the length of the list
print(f'\nLength of {sliceList} is {len(sliceList)}')

# max function - find the maximum value of the list
print(f'\nMaximum of {a} is {max(a)}')

# min function - find the minimum value of the list
print(f'\nMinimum of {a} is {min(a)}')

# sum function - find the sum of the value in the list
print(f'\nSum of {a} is {sum(a)}')

# Average using sum function - find the sum of the value in the list
print(f'\nAverage of {a} is {sum(a)/len(a)}')

# # Calculate average from user input until it is done
# average = list()
# print('\nAverage Calculation\n')
# while(True):
#     new_elem = input('Enter a number')
#     if new_elem == 'done': break
#     value = float(new_elem)
#     average.append(value)
# print(f'\nAverage of the entered input {average} is {sum(average)/len(average)}')

# Strings into list and list into strings
strings = 'Hello Senthur Athiban'
splittedList = strings.split()
print(f'\nSplitting "{strings}" string into list {splittedList}')
strings = 'Hello-Senthur-Athiban'
splittedList = strings.split('-')
print(f'\nSplitting "{strings}" string into list {splittedList}')
print(f'\nJoining "{splittedList}" List into string {'-'.join(splittedList)}')

# Sorting a list
org = [4,2,5,3,1]
print(f'\nBefore Sorting {org}')
org.sort()
print(f'\nAfter Sorting with <List>.sort() method\nOrginal list {org}\nSorted list {org}\n')
org = [4,2,5,3,1]
print(f'\nBefore Sorting {org}')
print(f'\nAfter Sorting with sorted() method\nOrginal list {org}\nSorted list {sorted(org)}\n')
org = [4,2,5,3,1]
org_copy = org[:]
org.sort()
print(f'\nBefore Sorting {org_copy}')
print(f'\nAfter Sorting with orginal backup using [:]\nOrginal list {org_copy}\nSorted list {org}')


# Array and List comparision
import numpy as np

new_array = np.array([1,2,3,4,5])
new_List = [1,2,3,4,5]

print(f'\nArray List Comparision\nArithmetic operators can be used in array but not in list\nArray ({new_array}/2) is {new_array/2}')
# print(f'List {new_List}/2 is {new_List/2}')
print(f'\nList can contain different datatypes but array can contain same datatype')
new_array = np.array([1,2,3,4,5,'test'])
new_List = [1,2,3,4,5,'test']
print(f'\n{new_array} -> all elements will be of type string\n{new_List} -> elements are stored with different datatypes')

# List Comprehension
a = [1,2,3]
b = [i*2 for i in a]
print(f'\nMultiplying elements with 2 using List comprehension on list {a} -> [i*2 for i in a]\n{b}')
stringList = 'Python'
print(f'\nUsing List comprehension {stringList}\n{[letter for letter in stringList]}')
a = [-1,5,0,-4,-3,1,2]
print(f'\nCondtions of positive numbers using List comprehension {a}\n{[i for i in a if i>=0]}')

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

inputText = input("\n Enter the sentence to filter the consonants: ")
print(f'\nInput Sentence : "{inputText}"\nconsonants: {[letter for letter in inputText if is_consonant(letter)]}')

