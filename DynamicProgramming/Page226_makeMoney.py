n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력 받기
moneyList = []
for i in range(n):
    moneyList.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)
print("d는 이렇다", d)

# 다이나믹 프로그래밍 바텀업
d[0] = 0
for i in range(n):
    print('화폐 종류 첫번째', i)
    for j in range(moneyList[i], m+1):
        print(moneyList[i], '부터', m+1, '까지')
        print('moneylist[i]는? : ', moneyList[i])
        if d[j-moneyList[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-moneyList[i]] + 1)
            print("d[j]: ", d[j])
            print('d[j-moneyList[i]] + 1: ', d[j-moneyList[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
