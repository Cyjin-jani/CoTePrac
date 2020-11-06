import copy
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


turnoff = graph
turnon = copy.deepcopy(graph)


def dfs(x, y):
    if x >= n or y >= m or x <= -1 or y <= -1:
        return False

    if turnoff[x][y] == 0:
        # 미방문인 경우 방문처리
        turnoff[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출함.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    # 이미 방문한 노드인 경우엔 false처리.
    return False


def dfs_rev(x, y):
    if x >= n or y >= m or x <= -1 or y <= -1:
        return False

    if turnon[x][y] == 1:
        # 미방문인 경우 방문처리
        turnon[x][y] = 0
        # 상하좌우의 위치도 모두 재귀적으로 호출함.
        dfs_rev(x - 1, y)
        dfs_rev(x + 1, y)
        dfs_rev(x, y - 1)
        dfs_rev(x, y + 1)
        return True
    # 이미 방문한 노드인 경우엔 false처리.
    return False


# 모든 노드(위치)에 대하여 아이스크림만들기
result = 0
res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
        if dfs_rev(i, j) == True:
            res += 1

print(result, res)


# 5 6
# 0 0 1 0 1 1
# 0 1 1 0 0 0
# 0 0 1 0 0 0
# 1 1 1 1 1 1
# 0 0 0 1 0 0
