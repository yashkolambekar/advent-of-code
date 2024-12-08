import re

total = 0

with open("input.txt", "r") as f:
    data = f.read()
    finds = re.findall(r"mul\(([0-9]*),([0-9]*)\)", data)
    
    for set in finds:
        product = int(set[0]) * int(set[1])
        total += product
        
    print(total)