L = int(input())

for _ in range(L):
    n, k1, alpha = map(int, input().split())
    visited = set()
    current = k1
    while current not in visited:
        visited.add(current)
        current = k1 + alpha * (current ** 2) % n
    print(len(visited))
