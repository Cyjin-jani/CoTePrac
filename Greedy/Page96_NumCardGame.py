n, m = map(int, input().split())

result = 0

# for i in range(n):
#     row = list(map(int, input().split()))
#     minNum = min(row)

#     result = max(result, minNum)

# print(result)


# 다른 풀이

for i in range(n):
    row = list(map(int, input().split()))
    row.sort()
    minValue = row[0]

    result = max(result, minValue)

print(result)
