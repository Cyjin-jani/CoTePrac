list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11, 22, 33]


list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]


print("list1 : {}, list2 : {}".format(list1, list2))


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
