def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    if list1 == list2: 
        return True
    else:
        return False


print(permutation([1,2,3],[2,3,1]))
print(permutation(['a','b','c'],['b','c','a']))
print(permutation([1,2,3],[3,3,1]))
print(permutation(['a','b','d'],['b','c','a']))