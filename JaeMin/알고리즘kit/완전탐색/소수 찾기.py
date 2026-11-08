from itertools import permutations  
def solution(numbers):
    def is_prime (n):
        if n < 2:
            return 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return 0
        return 1 
    
    N = len(numbers)
    n_set = set()
    for i in range(1, N+1):
        arr = permutations(numbers,i)
        for x in arr:
            num = int("".join(x))
            n_set.add(num)
    
    ans = 0
    for x in n_set:
        if is_prime(x):
            ans += 1
    return ans