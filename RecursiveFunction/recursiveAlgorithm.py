# def sum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + sum(n-1)


# a = int(input("Number: "))
# print(sum(a))


# 반복적 프로그래밍
def solution(x):
    answer = []
    for i in range(x+1):
        if i == x+1:
            return
        if len(answer) >= 2:
            answer.append(answer[i-2]+answer[i-1])
        else:
            answer.append(i)
    return answer[x]


# 재귀함수 이용하기


def solutions(x):
    if x < 2:
        return x
    else:
        return solutions(x-2) + solutions(x-1)


# #조합의 경우의 수 계산
# from math import factorial as f

# def combi(n, m):
#     return f(n)/ (f(m) * f(n-m))

# 재귀함수를 이용한 경우.

# def combi(n, m):
#     if n == m:
#         return 1
#     elif m == 0:
#         return 1
#     else:
#         return combi(n-1, m) + combi(n-1, m-1)


# 이진탐색 재귀알고리즘

def binaryRecursive(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binaryRecursive(L, x, l, mid-1)

    else:
        return binaryRecursive(L, x, mid+1, u)
