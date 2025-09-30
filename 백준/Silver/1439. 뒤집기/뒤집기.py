n = input()

count = 0
answer = []
flag = False

#다 1로 바꿔야 할 때
for i in n:
    if i == '0' and flag == False:
        count += 1
        flag = True
    elif i == '1':
        flag = False

answer.append(count)

flag = False
count = 0
# 다 0으로 바꿔야 할 때
for i in n:
    if i == '1' and flag == False:
        count += 1
        flag = True
    elif i == '0':
        flag = False
answer.append(count)

print(min(answer))