def solution(s):
    answer = True
    balance = 0
    
    for i in s:
        if balance == -1:
            return False
        if i == '(':
            balance += 1
        else:
            balance -= 1
    
    if balance != 0:
        return False
        
    return answer