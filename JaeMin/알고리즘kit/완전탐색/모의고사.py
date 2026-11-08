def solution(answers):
    N = len(answers)
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    p1 = 0
    p2 = 0
    p3 = 0
    for i in range(N):
        if answers[i] == pattern1[i % 5]:
            p1 += 1 
        if answers[i] == pattern2[i % 8]:
            p2 += 1 
        if answers[i] == pattern3[i % 10]:
            p3 += 1 
    max_ans = max(p1, p2, p3)
    answer = []
    if p1 == max_ans:
        answer.append(1)
    if p2 == max_ans:
        answer.append(2)
    if p3 == max_ans:
        answer.append(3)

    return answer