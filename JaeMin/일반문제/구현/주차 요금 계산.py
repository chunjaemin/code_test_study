#출차 기록없으면 23:59분 출차로 계산 
#시간이 딱떨어지지 않으면 올림으로 계산 
#청구할 주차 요금 계산 
#한 차가 하루에 두번 나갔다 들어갔다 하는건 아니겠지? 여러번들어가네 ㅇㄴ 
import math
from collections import defaultdict, deque 
def solution(fees, records):
    def calfee(m):
        add_m = max(0, m - fees[0])
        if add_m % fees[2] != 0:
            add_m = add_m - (add_m % fees[2]) + fees[2]
        add_fee = (add_m // fees[2]) * fees[3] 
        # print("m:", m, "add_m:", add_m, "add_fee", add_fee)
        return fees[1] + add_fee 
    
    def to_min(s):
        h, m = map(int, s.split(":"))
        return h * 60 + m 
        
    car_dict = defaultdict(lambda : {"in": deque(), "out" : deque()})
    #IN 할 때 out을 23:59로 미리 기록 
    for s in records:
        time, car, io_type = s.split(" ")
        if io_type == "IN":
            car_dict[car]["in"].append(time)  
        elif io_type == "OUT":
            car_dict[car]["out"].append(time)
    # for x in car_dict:
    #     print(x, car_dict[x])
    
    car_list = []
    for k in car_dict.keys():
        car_list.append(k)
    car_list.sort()
    
    car_idx = {}
    for i in range(len(car_list)):
        car_idx[car_list[i]] = i
    
    answer = [0] * len(car_list)
    for k, l in car_dict.items():
        iq = l["in"]
        oq = l["out"]
        i_m = 0 
        o_m = 0 
        while iq: 
            x = iq.popleft()
            if not oq:
                y = "23:59"
            else:
                y = oq.popleft()
            
            i_m += to_min(x)
            o_m += to_min(y)

        m = o_m - i_m
        fee = calfee(m)
        answer[car_idx[k]] = fee 
    
    return answer