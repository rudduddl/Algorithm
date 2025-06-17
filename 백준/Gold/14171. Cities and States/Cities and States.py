from collections import Counter

L = int(input())
pairs = []

for _ in range(L):
    city, state = input().split()
    city_prefix = city[:2]
    if city_prefix != state:
        pairs.append((city_prefix, state))

pair_counter = Counter(pairs)
answer = 0

for (a, b) in pair_counter:
    if (b, a) in pair_counter:
        answer += pair_counter[(a, b)] * pair_counter[(b, a)]


print(answer // 2)

    
