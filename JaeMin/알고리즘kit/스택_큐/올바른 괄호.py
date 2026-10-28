def solution(s):
    ans = True
    q = []
    for x in s: 
        if x == '(':
            q.append('(')
        if x == ')':
            if len(q) != 0:
                q.pop()
            else:
                ans = False
    if len(q) != 0:
        ans = False

    return ans 