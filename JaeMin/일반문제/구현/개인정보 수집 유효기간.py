def solution(today, terms, privacies):
    def to_day(a,b,c):
        aa = int(a)
        bb = int(b)
        cc = int(c)
        return aa*28*12 + bb*28 + cc 
    
    td = {}
    ans = []

    today_a, today_b, today_c = today.split(".")
    for s in terms:
        a, b = s.split(" ")
        td[a] = b 
    
    for i, s in enumerate(privacies):
        day, term= s.split(" ")
        a, b, c = day.split(".")
        
        if to_day(today_a,today_b,today_c) - to_day(a,b,c) >= to_day(0, td[term], 0):
            ans.append(i+1)
            
    return ans