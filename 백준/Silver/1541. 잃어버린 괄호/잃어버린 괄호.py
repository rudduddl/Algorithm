expr = input().split("-")

answer = sum(map(int, expr[0].split('+')))

for e in expr[1:]:
    answer -= sum(map(int, e.split("+")))

print(answer)