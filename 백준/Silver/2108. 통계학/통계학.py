import sys
from collections import Counter

n = int(sys.stdin.readline())

datas = []

for _ in range(n):
    datas.append(int(sys.stdin.readline()))

datas.sort()

print(round(sum(datas) / len(datas)))
print(datas[len(datas)//2])

counter = Counter(datas)

most_common_list = counter.most_common()

max_freq = most_common_list[0][1]

max_list = []

for item, freq in most_common_list:
    if freq == max_freq:
        max_list.append(item)
    else:
        break
        
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])

print(max(datas) - min(datas))