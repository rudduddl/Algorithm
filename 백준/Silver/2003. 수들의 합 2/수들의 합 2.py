import sys
n, m = map(int, input().split())

num_list = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
current_sum = 0
count = 0

while True:
    if current_sum >= m:
        if current_sum == m:
            count += 1
        current_sum -= num_list[left]
        left += 1
    elif right == n:
        break
    else:
        current_sum += num_list[right]
        right += 1

print(count)