n = int(input())

sorted_ropes = sorted((int(input()) for _ in range(n)), reverse=True)

answer = []

for i in range(n):
    answer.append(sorted_ropes[i] * (i+1))

print(max(answer))