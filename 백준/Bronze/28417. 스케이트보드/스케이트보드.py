max_score = -100000
for _ in range(int(input())):
    sum_score = 0
    score = list(map(int, input().split()))
    run_score = [score.pop(0) for _ in range(2)]
    run_score = max(run_score)
    
    score.sort(reverse=True)
    sum_score += run_score
    sum_score += score.pop(0) + score.pop(0)

    if max_score < sum_score:
        max_score = sum_score
    

print(max_score)