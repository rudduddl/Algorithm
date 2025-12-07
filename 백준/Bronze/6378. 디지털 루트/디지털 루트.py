import sys

def digital_sum(num):
    while len(num) > 1:
        digit_root = 0
        for i in str(num):
            digit_root += int(i)
        num = str(digit_root)

    return int(num)

while(True):
    n = sys.stdin.readline().strip()
    if n == "0":
        break

    print(digital_sum(n))