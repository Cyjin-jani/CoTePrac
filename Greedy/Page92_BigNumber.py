# array_size, plus_count, in_row = map(int, input().split())
# dataList = list(map(int, input().split()))

# 출력예시 데이터 넣기 (굳이 입력받지 않음)
array_size = 5
plus_count = 8
in_row = 3
randomArray = [2, 4, 5, 4, 6]

################### 내 풀이 ###################

# 배열 오름차순 정렬
randomArray.sort()
# 가장 큰 수와 그다음 큰 수 찾기
largestNum = randomArray[len(randomArray)-1]
nextNum = randomArray[len(randomArray) - 2]
# 결과값
result = 0
# 카운트
count = 0

# 가장 큰 수를 in_row만큼 더하고 두 번째로 큰 수를 한 번 더하는 연산을 plus_count만큼 반복
for i in range(plus_count):
    for j in range(in_row):
        print("largestNum", largestNum)
        result += largestNum
        count += 1
        print(result, count)
    result += nextNum
    count += 1
    print(result, count)
    if count == plus_count:
        print("result", result)
        break


################### 정답 풀이 ###################
# 배열의 크기: n, 숫자가 더해지는 횟수: m, 연속연산횟수: k
# n,m,k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수 정렬
data.sort()
# 가장 큰 수
first = data[n-1]
# 두 번째로 큰 수
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

# 최종답안 출력
print(result)
