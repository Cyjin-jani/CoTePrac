
# 나의 풀이

arraylen = int(input())
numList = []
for i in range(arraylen):
    numList.append(input())

numList.sort(reverse=True)

for num in numList:
    print(num, end=' ')


# 책 답안 예시
# N을 입력받기

n = int(input())

# N개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과 출력
for i in array:
    print(i, end=' ')
