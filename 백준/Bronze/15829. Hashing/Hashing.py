N = int(input())
user_input = input()

m = 1234567891
r = 31
answer = 0


for i in range(len(user_input)):
    num = ord(user_input[i]) - 96
    answer += num * (r ** i)

print(answer % m)
