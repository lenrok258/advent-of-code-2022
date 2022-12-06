# test: 
# input: 1760

input_line = open('input.txt', 'r').read()

for i in range(4, len(input_line)):
    quarduple = input_line[i-4:i]
    if len(set(quarduple)) == 4:
        print(f"Unique quarduple: {quarduple}, index: {i}")
        break