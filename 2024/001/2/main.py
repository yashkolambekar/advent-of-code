import math

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return mergeSort(less) + [pivot, ] + mergeSort(great)
    
# Taken from google
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
        
        
        
def count_reps(arr, target):
    position = binary_search(arr, target)
    if (position == -1):
        return 0
    while arr[position] == target:
        if(position == 0):
            break
        position -= 1  
    position += 1 
    target_position = position
    while arr[target_position] == target:
        if(target_position == (len(arr) - 1)):
            break
        target_position += 1 
    target_position -= 1  
    return (abs(target_position - position) + 1)

array_1 = []
array_2 = []

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    for i in data:
        temparr = i.split("   ")
        array_1.append(int(temparr[0]))
        array_2.append(int(temparr[1]))
        

array_1 = mergeSort(array_1)
array_2 = mergeSort(array_2)

error = 0

for i in array_1:
    # print(i)
    reps = count_reps(array_2, i)
    # print(reps)
    localerror = i * reps
    error += localerror
    
print(error)