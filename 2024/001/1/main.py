import math

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return mergeSort(less) + [pivot, ] + mergeSort(great)

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

distance = 0

for i in range(len(array_1)):
    local_distance = abs(array_1[i] - array_2[i])
    distance += local_distance
    
print(distance)
