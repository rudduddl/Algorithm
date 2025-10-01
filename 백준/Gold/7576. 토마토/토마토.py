from collections import deque
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]


queue = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            queue.append((x,y))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
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
            