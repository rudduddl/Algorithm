N, money = map(int, input().split())

coins = [int(input()) for _ in range(N)]
sorted_coins = sorted(coins, key=lambda x : -x)

count = 0
for coin in sorted_coins:
    if money % coin != money :
        count += (money // coin)
        money = money % coin

print(count)