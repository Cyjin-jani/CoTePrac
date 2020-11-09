# 나의 풀이

n, k = map(int, input().split())

aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
result = 0

aList.sort()
bList.sort(reverse=True)

# k만큼 돌면서 교체하기
for i in range(k):
    # b배열에서 a배열 원소가 더 작은 경우 교체를 진행.
    for j in range(len(bList)):
        if aList[i] < bList[j]:
            aList[i], bList[j] = bList[j], aList[i]
            break

# a배열의 원소들 총 합 구하기
for num in aList:
    result += num

print(result)


# 모범 답안 예시
n, k = map(int, input().split())  # N과 K를 입력 받기
a = list(map(int, input().split()))  # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split()))  # 배열 B의 모든 원소를 입력받기

a.sort()  # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))  # 배열 A의 모든 원소의 합을 출력
