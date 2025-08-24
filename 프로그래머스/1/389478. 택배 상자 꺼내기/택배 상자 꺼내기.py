
def solution(n, w, num):
    height = (n+w+1) // w
    
    count = 1
    boxes = [[0 for j in range(w)] for i in range(height)]
    
    
    
    for i in range(height):
        if i % 2 != 0:
            for j in range(w-1,-1,-1):
                if count > n:
                    break
                boxes[i][j] = count
                count += 1
        else:
            for j in range(w):
                if count > n:
                    break
                boxes[i][j] = count
                count +=1
    
    answer = 0
    count = None
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] == num:
                count = j
            if count == j:
                answer += 1
                if boxes[i][j] == 0:
                    answer -= 1
                
            
    
    
    
    
    return answer