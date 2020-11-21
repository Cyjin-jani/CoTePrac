from collections import defaultdict

tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]


def dfs(lenti, graph, N, key, footprint):
    print('발자취', footprint)

    if len(footprint) == N + 1:
        return footprint
    print("for 전 graph[key]", graph[key])

    for idx, country in enumerate(graph[key]):
        print('idx', idx, 'country', country)
        graph[key].pop(idx)
        print("graph[key]", graph[key])

        tmp = footprint[:]
        print('tmp', tmp)
        tmp.append(country)
        print('tmp에 country가 추가됨', tmp)

        ret = dfs(lenti, graph, N, country, tmp)
        print('ret', ret)

        graph[key].insert(idx, country)
        print("insert후의 idx와 key와 graph[key]", idx, key, graph[key])

        if ret:
            print("ret????: ", ret)
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
        print(graph)

    answer = dfs(len(tickets), graph, N, "ICN", ["ICN"])

    return answer


solution(tickets)
