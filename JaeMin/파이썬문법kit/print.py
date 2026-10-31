
# 1. 기본 출력
print(a, b)                 # 10 20
print(f"{a=}, {b=}")        # a=10, b=20 (디버깅)

# 2. 구분자 / 줄바꿈
print(a, b, sep=",")        # 10,20
print(a, end=" ")           # 줄바꿈 없이 출력

# 3. 배열 출력 ★
arr = [1, 2, 3]
print(arr)                  # [1, 2, 3]
print(*arr)                 # 1 2 3
print(*arr, sep="\n")       # 원소별 줄바꿈

# 4. 문자열 연결
print(" ".join(map(str, arr)))  # 1 2 3

# 5. 2차원 배열 출력 ★
board = [[1, 2], [3, 4]]
for row in board:
    print(*row)

# 6. 소수점 출력
print(f"{3.14159:.2f}")     # 3.14
