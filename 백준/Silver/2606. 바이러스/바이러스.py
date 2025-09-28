computer = int(input())
m = int(input())

graph = [[] for _ in range(computer+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer + 1)


def worm(start):
    count = 0
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            for nxt in graph[node]:
                if not visited[nxt]:
                    stack.append(nxt)
                    
    return count

print(worm(1) - 1)