
from heapq import heappush, heappop, heapify

# =========================
# 1. 최소 힙 (기본) ★
# =========================
heap = []

heappush(heap, 5)
heappush(heap, 2)
heappush(heap, 8)
heappush(heap, 1)

print(heap[0])        # 1 (최솟값 조회)
print(heappop(heap))  # 1 (최솟값 제거 및 반환)
print(len(heap))      # 힙 크기

# 모든 원소 오름차순 꺼내기
while heap:
    print(heappop(heap))


# =========================
# 2. 최대 힙 (음수 활용) ★
# =========================
heap = []

heappush(heap, -5)
heappush(heap, -2)
heappush(heap, -8)

print(-heap[0])        # 8 (최댓값 조회)
print(-heappop(heap))  # 8 (최댓값 제거)


# =========================
# 3. 리스트 → 힙 변환
# =========================
arr = [5, 3, 8, 1, 2]

heapify(arr)           # O(N)
print(heappop(arr))    # 1


# =========================
# 4. 튜플 우선순위 큐 ★
# =========================
heap = []

heappush(heap, (2, "B"))
heappush(heap, (1, "A"))
heappush(heap, (3, "C"))

print(heappop(heap))   # (1, 'A')

# 첫 번째 값 우선, 같으면 두 번째 값 비교
heappush(heap, (1, 5))
heappush(heap, (1, 3))
# 위처럼 자료형이 다른 두 번째 값은
# 우선순위가 같을 때 비교 오류가 날 수 있음


# =========================
# 5. K번째로 작은 값
# =========================
arr = [7, 2, 5, 1, 9]
heapify(arr)

k = 3
for _ in range(k):
    x = heappop(arr)

print(x)               # 5


# =========================
# 6. 시간 복잡도
# =========================
# heappush() : O(log N)
# heappop()  : O(log N)
# heap[0]    : O(1)
# heapify()  : O(N)
