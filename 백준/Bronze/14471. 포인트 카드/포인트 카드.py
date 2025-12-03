n, m = map(int, input().split())

cards = []
for _ in range(m):
    cards.append(list(map(int, input().split())))

sorted_cards = sorted(cards, key=lambda x : -x[0])
gift = 0
money = 0

for card in sorted_cards:
    if gift == m-1:
        break
    elif card[0] >= n:
        gift += 1
    elif card[1] + card[0] >= n:
        money += abs(card[0] - n)
        gift += 1

print(money)