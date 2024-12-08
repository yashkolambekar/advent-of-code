def check_safety(arr):
    is_safe = True
    increasing = True
    first_diff_checked = False
    
    for i in range(len(arr)):
        if i == (len(arr) - 1):
            break
        diff = abs(arr[i] - arr[i + 1])
        if diff < 1 or diff > 3:
            is_safe = False
            break
        if arr[i] < arr[i + 1]:
            if not(first_diff_checked):
                first_diff_checked = True
            if first_diff_checked and not(increasing):
                is_safe = False
                break
        elif arr[i] > arr[i + 1]:
            if not(first_diff_checked):
                increasing = False
                first_diff_checked = True
            elif increasing:
                is_safe = False
                break
    return is_safe                
    

safe_data_count = 0

with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        data[i] = [int(j) for j in data[i]]
        if check_safety(data[i]):
            safe_data_count += 1
print(safe_data_count)        