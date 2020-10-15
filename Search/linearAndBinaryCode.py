
# 선형 탐색의 코드
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1


# 이진 탐색 코드
def solution(L, x):
    lower = 0
    upper = len(L) - 1

    while(lower <= upper):
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1

    return -1
