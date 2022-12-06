# test: 
# input: 2974

input_line = open('input.txt', 'r').read()

for i in range(14, len(input_line)):
    message_preambula = input_line[i-14:i]
    if len(set(message_preambula)) == 14:
        print(f"message_preambula: {message_preambula}, index: {i}")
        break