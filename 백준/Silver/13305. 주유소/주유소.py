n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total = 0

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    total += min_price * dist[i]

print(total)