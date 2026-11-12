from collections import defaultdict
def solution(id_list, report, k):
    id_dict = { key : i for i, key in enumerate(id_list)}
    ans = [0] * len(id_list)
    rl = defaultdict(int)
    ml = defaultdict(list)
    
    for s in report:
        a, b = s.split(" ")
        if a not in ml[b]:
            rl[b] += 1 
            ml[b].append(a)
    
    for key, v in rl.items():
        if v >= k:
            for name in ml[key]:
                ans[id_dict[name]] += 1
    return ans