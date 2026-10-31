# 주는 사람 기준? vs 받는 사람 기준? 
# 양 옆에서 모두 받을 수 있다면 아무한테나 받아도 결과에 영향이 없을까? 
# 결과에 영향이 있음 잘 선택해야 됨 
# 이 지점에서 그리디 vs dfs 인지 구분해야하는 분기가 생길 수도? 
# 문제에는 그리디라고 적혀있긴 한데 실제로 모른다고 가정하면 dfs도 옵션으로 염두해두고 있어야 하지않나? 이건 AI한테 물어봐야 할 듯 
# 누굴 선택해야할지 항상 구분이 가능하면 그리디이고 아니라면 dfs아니려나

#이거근데 그냥 가장 앞에서부터 받아야 하는 사람이 왼쪽부터 짚으면 되는거 아닌가? 맨 왼쪽 사람이 오른쪽을 가져가서 그다음 사람이 못받아도 어차피 쌤썜인데, 맨 왼쪽 사람이 안가져가면 확정으로 못받으니까 그냥 무조건 가져갈 수 있는거 가져가야 되네 => 그리디 맞는거같은데 이럼 


#풀이후기
#와 예외처리가 너무 많다 
#여벌 옷 가져온 애가 도둑맞을 수 있다는건 문제 대충 읽었으면 놓치는 구조고 
#심지어 제공되는 예시는 정렬되어있는데 입력값이 정렬되어 있지 않다는 고지도 없는데, 정렬되어 있지 않을걸 예상해서 정렬까지..? 이건 너무 불친절 한 것 같음 

def solution(n, lost, reserve):
    l_list = [0] * (n+2) 
    r_list = [0] * (n+2)
    real_lost = []

    for x in reserve:
        r_list[x] = 1
    
    cnt = n - len(lost)
    lost.sort()
    reserve.sort()
    for x in lost: 
        if r_list[x] == 1:
            r_list[x] = 0
            cnt += 1 
        else:
            real_lost.append(x)
    
    for x in real_lost: 
        if r_list[x-1] == 1:
            r_list[x-1] = 0
            cnt += 1
        elif r_list[x+1] == 1:
            r_list[x+1] = 0
            cnt += 1
    answer = cnt 
    return answer