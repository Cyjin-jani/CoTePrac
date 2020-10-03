n, k = map(int, input().split())

### 내 풀이 ###
count = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n / k
        count += 1
    else:
        # 나누어 떨어지지 않는 경우 뺴기 1을 해야함.
        n -= 1
        count += 1

print(count)


########## 문제집 답안 - 단순하게 푸는 답안 (답안이 좀 이상) ##########

# result = 0
# # n이 k이상이라면 k로 계속 나누기.
# while n >= k:
#     # n이 k로 나누어 떨어지지 않는다면 N에서 1씩 빼기
#     while n % k == 0:
#         n -= 1
#         result += 1
#     # k로 나누기
#     n //= k
#     result += 1

# # 마지막으로 남은 수에 대하여 1씩 빼기
# while n > 1:
#     n -= 1
#     result += 1

# print(result)


########## 문제집 답안  - n이 100억 이상의 큰 수가 되는 경우 가정했을때 ##########

result = 0

while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
