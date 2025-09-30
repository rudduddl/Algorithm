n = int(input())

sorted_people = sorted(map(int, input().split()))

answer = 0
time = 0

for i in sorted_people:
    time += i
    answer += time

print(answer)