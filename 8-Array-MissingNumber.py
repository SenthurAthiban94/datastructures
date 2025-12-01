# Arithmetic Progression (N*(N+1)//2)
# # You can use the arithmetic progression formula to find the sum of the numbers from 1 to n 
# and then subtract the sum of the numbers in the array to get the missing number.
def missing_number(arr, n):
    totalnumberSum = n * (n+1) //2
    sumarray = sum(arr)
    missing = (totalnumberSum) - sumarray
    return missing
    # for i in range(n):
    #     if (i+1) not in arr: return (i+1)
        