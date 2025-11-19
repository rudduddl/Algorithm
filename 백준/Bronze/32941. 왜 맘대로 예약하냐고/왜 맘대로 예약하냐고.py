t, x = map(int, input().split())
n = int(input())

count = 0

for _ in range(n):
    info = int(input())
    numbers = list(map(int, input().split()))
    if x not in numbers:
        continue
    else:
        count += 1

if count == n:
    print("YES")
else:
    print("NO")