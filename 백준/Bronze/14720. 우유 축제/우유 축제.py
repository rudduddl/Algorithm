n = int(input())

cnt = 0

milk = list(map(int, input().split( )))[:n]

tmp = 0
for i in milk:
    if i == tmp:
        if tmp == 0:
            cnt += 1
            tmp = 1
        elif tmp == 1:
            cnt += 1
            tmp = 2
        else:
            cnt += 1
            tmp = 0

print(cnt)