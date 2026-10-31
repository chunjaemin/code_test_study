def solution(numbers, target):
    N = len(numbers)
    cnt = 0 
    def dfs(arr, depth):
        nonlocal cnt 
        if depth == N:
            if sum(arr) == target:
                cnt += 1  
        else:
            arr.append(numbers[depth])
            dfs(arr, depth + 1)
            arr.pop()
            
            arr.append(-numbers[depth])
            dfs(arr, depth + 1)
            arr.pop()
    dfs([], 0)
    ans = cnt 
    return ans