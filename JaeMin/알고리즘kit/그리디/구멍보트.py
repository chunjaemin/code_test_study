#마지막에 남은 애들 보트 탓는지 어떻게 구분함?
#마지막 남은 애는 모든케이스가 r == l 임 이걸로 예외잡기
def solution(people, limit):
    people.sort()
    l = 0
    r = len(people) - 1
    
    cnt = 0
    while l<=r:
        if l == r:
            cnt += 1 
            break 
        if people[l] + people[r] <= limit:
            cnt += 1
            l += 1
            r -= 1
        else:
            cnt += 1
            r -= 1
    
    return cnt