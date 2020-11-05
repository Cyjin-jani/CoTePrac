# n, m을 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위 파악하기. n*m보다 더 큰 좌표값은 없으며, -1이 되어도 안됨. (0 혹은 1임)
    if x >= n or y >= m or x <= -1 or y <= -1:
        return False
    # 현재 노드를 방문했는지 여부 파악
    if graph[x][y] == 0:
        # 미방문인 경우 방문처리
        graph[x][y] = 1
        # 상하좌우의 위치도 모두 재귀적으로 호출함.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    # 이미 방문한 노드인 경우엔 false처리.
    return False


# 모든 노드(위치)에 대하여 아이스크림만들기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)
