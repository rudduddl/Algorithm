from collections import defaultdict

def solution(clothes):
    type_count = defaultdict(int)
    
    for name, type_ in clothes:
        type_count[type_] += 1
    
    answer = 1
    for count in type_count.values():
        answer *= (count + 1)
    
    return answer - 1