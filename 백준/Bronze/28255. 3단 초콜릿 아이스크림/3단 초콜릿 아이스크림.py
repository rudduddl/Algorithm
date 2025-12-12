import math
for i in range(int(input())):
    s = input()
    len_pre = math.ceil(len(s) / 3)

    pre = s[:len_pre]
    reversed_s = pre[::-1]

    tail_rev_s = reversed_s[1:]
    tail_s = pre[1:]

    box = []
    flag = False

    s1 = pre + tail_rev_s + pre
    s2 = pre + reversed_s + pre
    s3 = pre + tail_rev_s + tail_s
    s4 = pre + reversed_s + tail_s

    if s == s1 or s == s2 or s == s3 or s == s4:
        flag = True

    if flag == True:
        print("1")
    else: 
        print("0")
        