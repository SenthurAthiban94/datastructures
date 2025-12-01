def findPairs(arr,target):
    for i in range(len(arr)):
         for j in range(i+1,len(arr)):
             if arr[i]==arr[j]:
                 continue
             elif arr[i]+arr[j] == target:
                 print(i,j)

def twoSum(arr,target):
    seen = {}
    for i,n in enumerate(arr):
        complement = target - n
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[n] = i
        

findPairs([1,2,3,2,3,4,5,6], 6)

print(twoSum([2, 7, 11, 15], 9))