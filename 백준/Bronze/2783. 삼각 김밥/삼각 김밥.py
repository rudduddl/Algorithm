x, y = map(int, input().split())
kimbaps = [round((x / y) * 1000, 2)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    kimbaps.append(round((a/b) * 1000, 2))

print(min(kimbaps))