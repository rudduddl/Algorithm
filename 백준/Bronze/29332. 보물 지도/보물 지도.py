n = int(input())

INF = 10**18

min_x = -INF
max_x = INF
min_y = -INF
max_y = INF

for _ in range(n):
    x, y, d = map(str, input().split())
    x, y = int(x), int(y)
    if d == "R":
        min_x = max(min_x, x)
    elif d == "L":
        max_x = min(max_x, x)
    elif d == "U":
        min_y = max(min_y, y)
    else:
        max_y = min(max_y, y)


if min_x + 1 >= max_x or min_y + 1 >= max_y:
    print(0)
elif min_x == -INF or max_x == INF or min_y == -INF or max_y == INF:
    print("Infinity")
else:
    print((max_x - min_x - 1) * (max_y - min_y - 1))