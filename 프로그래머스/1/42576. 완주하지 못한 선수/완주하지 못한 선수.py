def solution(participant, completion):
    result = {}
    
    for person in participant:
        if person in result:
            result[person] += 1
        else:
            result[person] = 1
            
    for person in completion:
        if person in result:
            result[person] -= 1

    for person in result:
        if result[person] == 1:
            return person
