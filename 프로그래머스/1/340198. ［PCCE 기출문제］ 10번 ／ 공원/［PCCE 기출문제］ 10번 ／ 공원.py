def solution(mats, park):
    n, m = len(park), len(park[0])
    
    for s in sorted(mats, reverse=True):
        if s > n or s > m:
            continue
            
        for i in range(n - s + 1):
            for j in range(m - s + 1):
                ok = True
                
                for x in range(i, i + s):
                    for y in range(j, j + s):
                        if park[x][y] != "-1":
                            ok = False
                            break
                    if not ok:
                        break
                            
                if ok:
                    return s
    return -1