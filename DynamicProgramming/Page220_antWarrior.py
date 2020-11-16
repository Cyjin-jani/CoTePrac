n = int(input())
k = list(map(int, input().split()))

# 계산된 결과를 저장하기 위해 DP테이블 초기화
d = [0] * 100

# 바텀업 방식
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    print("d[i-1], d[i-2], k[i]", d[i-1], d[i-2], k[i])
    d[i] = max(d[i-1], d[i-2]+k[i])
    print('d[i]', d[i])

print(d[n-1])
