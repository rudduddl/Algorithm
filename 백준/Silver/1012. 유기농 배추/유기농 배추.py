import sys
sys.setrecursionlimit(10**6)
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[False]*m for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = True

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if graph[y][x] == False:
            return
        
        #이미 방문한 배추임을 표시
        graph[y][x] = False
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == True:
                dfs(x, y)
                count += 1
    print(count)
