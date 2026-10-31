
from collections import Counter, defaultdict, deque

# =========================
# 1. Counter - 빈도수 계산
# =========================
arr = [1, 1, 2, 3, 3, 3]
cnt = Counter(arr)
# Counter({3: 3, 1: 2, 2: 1})

print(cnt[3])               # 3 (등장 횟수)
print(cnt[99])              # 0 (없는 키)
print(cnt.most_common(2))   # [(3, 3), (1, 2)]
print(cnt.most_common(1)[0]) # (3, 3)

print(cnt.keys())           # 키 목록
print(cnt.values())         # 빈도수 목록
print(cnt.items())          # (원소, 빈도수) 목록

for key, count in cnt.items():
    print(key, count)

# 문자열도 가능
cnt = Counter("banana")
# {'a': 3, 'n': 2, 'b': 1}


# =========================
# 2. defaultdict - 자동 초기화
# =========================
d = defaultdict(int)       # 기본값 0
d["a"] += 1
print(d["b"])               # 0

d = defaultdict(list)      # 기본값 []
d["a"].append(10)
d["a"].append(20)
print(d["a"])               # [10, 20]

d = defaultdict(set)       # 기본값 set()
d["a"].add(1)
d["a"].add(1)
print(d["a"])               # {1}

# 그룹핑 ★
arr = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)

for key, value in arr:
    groups[key].append(value)
# {'a': [1, 3], 'b': [2]}


# =========================
# 3. deque - 양방향 큐
# =========================
q = deque([1, 2, 3])

q.append(4)          # 오른쪽 추가
q.appendleft(0)      # 왼쪽 추가

q.pop()              # 오른쪽 제거 및 반환
q.popleft()          # 왼쪽 제거 및 반환 ★

print(q[0])          # 맨 앞 원소
print(q[-1])         # 맨 뒤 원소
print(len(q))        # 길이
print(list(q))       # 리스트 변환

q.rotate(1)          # 오른쪽으로 1칸 회전
q.rotate(-1)         # 왼쪽으로 1칸 회전

# 일반적인 큐 사용 ★
q = deque([1, 2, 3])

while q:
    x = q.popleft()
    print(x)

# BFS 기본 형태 ★
q = deque([start])
visited = {start}

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
