def solution(schedules, timelogs, startday):
    count = 0
    day_list = []
    is_late = False
    answer = 0
    new_time = 0
    
    for i in range(0,7):
        if startday + i > 7:
            count += 1
            day_list.append(count)
        else:
            day_list.append(startday+i)
            
    for i , logs in enumerate(timelogs):
        start_time = to_minutes(schedules[i] + 10)
        day = startday
        is_late = False
        
        for log in logs:
            if day not in (6,7):
                if to_minutes(log) > start_time:
                    is_late = True
                    break
            day = day + 1 if day % 7 != 0 else 1
            
        if not is_late:
            answer += 1

            
    return answer

def to_minutes(t):
    return (t // 100) * 60 + t % 100