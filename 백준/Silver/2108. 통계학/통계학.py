import sys

n = int(sys.stdin.readline())

datas = []

for _ in range(n):
    datas.append(int(sys.stdin.readline()))

datas.sort()

print(round(sum(datas) / len(datas)))
print(datas[len(datas)//2])

counts = {}
for i in datas:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
mx = max(counts.values())
max_list = []

for i in counts:
    if mx == counts[i]:
        max_list.append(i)
        
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])

print(max(datas) - min(datas))