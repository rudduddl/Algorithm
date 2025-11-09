import sys

n = int(input())

datas = []
for _ in range(n):
    datas.append(int(sys.stdin.readline()))

datas.sort()
print(*datas, sep="\n")