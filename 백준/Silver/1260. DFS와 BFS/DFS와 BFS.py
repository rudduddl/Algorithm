from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

# DFS
visited_dfs = set()
order_dfs = []
def dfs(v):
    if v in visited_dfs:
        return
    visited_dfs.add(v)
    order_dfs.append(v)
    for nxt in graph[v]:
        dfs(nxt)

dfs(v)
print(" ".join(map(str, order_dfs)))


#BFS
def bfs(start):
    visited_bfs = set()
    order_bfs = []
    queue = deque([start])
    visited_bfs.add(start)
    while queue:
        v = queue.popleft()
        order_bfs.append(v)
        for nxt in graph[v]:
            if nxt not in visited_bfs:
                visited_bfs.add(nxt)
                queue.append(nxt)
    
    return order_bfs

print(" ".join(map(str, bfs(v))))