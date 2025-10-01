from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))