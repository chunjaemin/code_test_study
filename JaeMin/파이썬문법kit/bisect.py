from bisect import bisect_left, bisect_right

arr = [1, 2, 2, 2, 3, 5, 7]

print(bisect_left(arr, 2))   # 1
print(bisect_right(arr, 2))  # 4

print(bisect_left(arr, 4))   # 5
print(bisect_right(arr, 4))  # 5

#구하고 싶은 것	코드
#| x 이상이 처음 나오는 위치 | 	bisect_left(a, x)
#| x 초과가 처음 나오는 위치 | 	bisect_right(a, x)
#| x 미만 개수 |	           bisect_left(a, x)
#| x 이하 개수 |               bisect_right(a, x)
#| x 이상 개수 |	           len(a) - bisect_left(a, x)
#| x 초과 개수 |	           len(a) - bisect_right(a, x)
#| x 등장 횟수 |	           bisect_left(a, x) - bisect_right(a, x)