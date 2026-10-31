
from itertools import combinations, permutations

arr = [1, 2, 3]

# =========================
# 1. combinations - 조합 ★
# 순서 상관 X, 중복 선택 X
# =========================
print(list(combinations(arr, 2)))
# [(1, 2), (1, 3), (2, 3)]

print(list(combinations(arr, 3)))
# [(1, 2, 3)]

# 모든 2개 조합 순회
for a, b in combinations(arr, 2):
    print(a, b)


# =========================
# 2. permutations - 순열 ★
# 순서 중요 O, 중복 선택 X
# =========================
print(list(permutations(arr, 2)))
# [(1, 2), (1, 3), (2, 1),
#  (2, 3), (3, 1), (3, 2)]

print(list(permutations(arr, 3)))
# 3! = 6개

# 길이 생략 시 전체 원소 순열
print(list(permutations(arr)))
# 3! = 6개


# =========================
# 3. 중복 허용 조합 / 순열
# =========================
from itertools import (
    combinations_with_replacement,
    product
)

# 중복 조합
print(list(combinations_with_replacement(arr, 2)))
# [(1, 1), (1, 2), (1, 3),
#  (2, 2), (2, 3), (3, 3)]

# 중복 순열 (데카르트 곱)
print(list(product(arr, repeat=2)))
# [(1, 1), (1, 2), (1, 3),
#  (2, 1), (2, 2), (2, 3),
#  (3, 1), (3, 2), (3, 3)]


# =========================
# 4. 코테 활용 ★
# =========================

# 두 수의 합이 target인 조합 개수
target = 5
cnt = 0

for a, b in combinations(arr, 2):
    if a + b == target:
        cnt += 1

print(cnt)  # 1

# 조합 결과의 합 구하기
for comb in combinations(arr, 2):
    print(sum(comb))

# 문자열 순열
s = "ABC"
print(["".join(p) for p in permutations(s, 2)])
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']


# =========================
# 5. 시간 복잡도
# =========================
# 조합: nCr
# 순열: nPr = n! / (n-r)!
# 중복 조합: (n+r-1)Cr
# 중복 순열: n**r
