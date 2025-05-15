def solution(nums):
    a = len(nums) // 2
    result = set(nums)
    
    if(len(result) > a):
        return len(nums) // 2
    else:
        return len(result)
    
    
    
    