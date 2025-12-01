n = int(input())
numbers = list(map(int, input().split()))[:n]

sorted_numbers = sorted(numbers)

print(sum(sorted_numbers[:2]))