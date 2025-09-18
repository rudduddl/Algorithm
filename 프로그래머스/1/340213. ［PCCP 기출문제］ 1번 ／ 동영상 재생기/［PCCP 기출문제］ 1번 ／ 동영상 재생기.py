from datetime import datetime, timedelta

def solution(video_len, pos, op_start, op_end, commands):
    
    def to_timedelta(t):
        dt = datetime.strptime(t, "%M:%S")
        return timedelta(minutes=dt.minute, seconds=dt.second)
    
    time_video = to_timedelta(video_len)
    time_pos = to_timedelta(pos)
    time_start = to_timedelta(op_start)
    time_end = to_timedelta(op_end)
    
    seconds = timedelta(seconds=10)
    
    for po in commands:
        if po == 'prev':
            if time_pos < timedelta(seconds=10):
                time_pos = timedelta(seconds=0)
                continue
            time_pos = time_pos - seconds
                
        elif po == 'next':
            if time_start <= time_pos <= time_end:
                time_pos = time_end
            if time_video - time_pos < seconds:                
                time_pos = time_video
                continue
            time_pos = time_pos + seconds
            
        if time_start <= time_pos <= time_end:
            time_pos = time_end
            
            
    total_seconds = int(time_pos.total_seconds())
    mm = total_seconds // 60
    ss = total_seconds % 60
    
    return f"{mm:02d}:{ss:02d}"
