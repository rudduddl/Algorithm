import sys

N = int(input())

meeting_times = []

for i in range(N):
    meeting_times.append(tuple(map(int, sys.stdin.readline().split())))

sorted_meeting_times = sorted(meeting_times, key=lambda x : (x[1], x[0]))

end_time = 0
count = 0
for time in sorted_meeting_times:
    if end_time <= time[0]:
        count += 1
        end_time = time[1]

print(count)