# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# return : [ICN, JFK, HND, IAD]

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
#     "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]

# tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]

# tickets = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]

tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]


def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        print("start, end", t1, t2)
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
        print('routes', routes)

    start = ['ICN']
    answer = []

    while start:
        print('while start', start)
        top = start[-1]
        print('top이', top, '여기 routes에 있니?', routes)
        if top not in routes or len(routes[top]) == 0:
            print('루트에 업슴')
            answer.append(start.pop())
            print("바뀐 answer", answer)
            print('바뀐 start', start)
        else:
            print('루트에 존재')
            start.append(routes[top].pop())
            print('바뀐 start', start)
            print('바뀐 routes', routes)
    answer.reverse()
    # print(answer)
    return answer


solution(tickets)
