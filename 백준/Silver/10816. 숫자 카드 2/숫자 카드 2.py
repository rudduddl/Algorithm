from collections import Counter

n = int(input())
cards = Counter(list(map(int, input().split())))
m = int(input())
m_cards = list(map(int, input().split()))

answer = [cards[x] for x in m_cards]
print(*answer)