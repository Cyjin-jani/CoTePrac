# 무한을 의미하는 값으로 10억을 설정.
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

# 2ㅊㅏ원 리스트 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신에게 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받아서 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정.
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행결과출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1
if distance >= INF:
    print('-1')
else:
    print(distance)
