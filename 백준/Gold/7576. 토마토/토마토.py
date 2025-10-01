from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]


queue = deque()
for y in range(m):
    for x in range(n):
        if graph[y][x] == 1:
            queue.append((x,y))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))

days = 0
for row in graph:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        days = max(days, value)

print(days - 1)
            