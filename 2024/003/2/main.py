import re

total = 0

def find_muls_and_multiply(data):
    local_total = 0
    finds = re.findall(r"mul\(([0-9]*),([0-9]*)\)", data)
    for set in finds:
        product = int(set[0]) * int(set[1])
        local_total += product
    return local_total
    

with open("input.txt", "r") as f:
    data = f.read()
    
    dont_splits = data.split("don't()")
    
    valid_commands = []
    valid_commands.append(dont_splits.pop(0))

    for section in dont_splits:
        local_do_spilts = str(section).split('do()')
        print(len(local_do_spilts))
        if len(local_do_spilts) > 1:
            for i in range(len(local_do_spilts)):
                if i == 0:
                    continue
                valid_commands.append(local_do_spilts[i])
        
    for section in valid_commands:
        local_total = find_muls_and_multiply(str(section))
        total += local_total
    
print(total)