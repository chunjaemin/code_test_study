from collections import defaultdict 

def solution(nums):
    po_dict = defaultdict(int)
    ans = 0
    for x in nums:
        if po_dict[x] == 0:
            ans += 1 
        po_dict[x] += 1
    
    max_num = len(nums) / 2
    if ans >= max_num:
        ans = max_num
        
    return ans