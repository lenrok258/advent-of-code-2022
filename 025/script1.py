from sys import argv
from tqdm import tqdm

# test: 
# input: 2-20=01--0=0=0=2-120

snafu_ns = open(argv[1], 'r').read().splitlines()

def toDec(snafu):
    dec = 0
    for i in range(len(snafu)):
        c = snafu[len(snafu) - 1 - i]
        power = 5**i
        if c == "-":
            dec -= 1 * power
        elif c == "=":
            dec -= 2 * power
        else:
            dec += int(c) * power
    return dec


def toQuinary(dec):
    if dec == 0:
        return '0'
    nums = []
    while dec:
        dec, r = divmod(dec, 5)
        nums.append(str(r))
    return ''.join(reversed(nums))


def toSnafu(quinary):
    snafu = ""
    carry = 0
    for c in reversed(quinary):
        if carry != 0:
            c = str(int(c) + carry)
            carry = 0
        if c == "3":
            snafu += "="
            carry = 1
        elif c == "4":
            snafu += "-"
            carry = 1
        elif c == "5":
            snafu += "0"
            carry = 1
        else:
            snafu += c
    return "".join(reversed(snafu))


sum_dec = sum([toDec(sns) for sns in snafu_ns])
print(f"sum dec: {sum_dec}")

sum_quinary = toQuinary(sum_dec)
print(f"sum quinary: {sum_quinary}")

sum_snafu  = toSnafu(sum_quinary)
print(f"sum snafu: {sum_snafu}")
