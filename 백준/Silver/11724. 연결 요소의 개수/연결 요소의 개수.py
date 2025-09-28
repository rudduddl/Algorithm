import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)

    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt)

count = 0
for node in range(1, n+1):
    if node not in visited:
        dfs(node)
        count += 1

print(count)