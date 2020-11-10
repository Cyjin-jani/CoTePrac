# 모범답안 풀이.

n, m = map(int, input().split())
# 떡 리스트
tList = list(map(int, input().split()))
tList.sort()

start = 0
end = max(tList)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for num in tList:
        if num > mid:
            total += num - mid
    # 떡의 양이 부족한 경우 더 많이 잘라야 한다. (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        # 최대한 덜 짤랐을 때가 정답이라 result에 미리 기록.
        result = mid
        start = mid + 1

print(result)
