def solution(sizes):
    max_a = max(max(a, b) for a, b in sizes)
    max_b = max(min(a, b) for a, b in sizes)
    answer = max_a*max_b
    return answer