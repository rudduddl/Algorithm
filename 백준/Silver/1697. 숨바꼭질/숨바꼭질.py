from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
visited[n] = 0

queue = deque([n])

while queue:
    x = queue.popleft()
    if x == k:
        break
    for nx in (x-1,x+1,x*2):
        if 0 <= nx < MAX and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(visited[k])