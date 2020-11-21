tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]


def dfs(start, tickets, result):
    print('----------------!!!!!!!! DFS 시작!!!!!!----------------')
    print('시작점:', start, '티켓현황:', tickets, '결과물: ', result)
    if len(tickets) == 0:
        return result
    for i, ticket in enumerate(tickets):
        print('i는??? : ', i, '시작점은?', start)
        if start == ticket[0]:
            print('출발점 맞는 티켓 있다!! start', start, '현재 검사하는 티켓:',
                  ticket, 'ticket[0]', ticket[0])
            end = ticket[1]
            tickets.pop(i)
            result.append(end)
            print('티켓 존재 시점에서 팝, 결과배열에 넣기', "잔여티켓: ", tickets, "결과배열: ", result)
            temp = dfs(end, tickets, result)
            print('dfs의 결과를 저장한 temp 값: ', temp)
            if len(temp) != 0:
                print('temp가뭔데??', temp)
                return temp
            print('len(result)-1 인덱스에 해당하는 값을 결과배열에서 pop: ',
                  result[len(result)-1])
            result.pop(len(result)-1)
            print('i는??? : ', i, '시작점은?', start, '끝점은?', end)
            tickets.insert(i, [start, end])
            print('티켓 환불됨. (재삽입): ', tickets)
        else:
            print('출발점이 맞는 티켓이 없다.')

    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!DFS의 끝!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return []


def solution(tickets):
    tickets.sort()
    # print(tickets)
    result = []
    start = "ICN"
    result.append(start)
    answer = dfs(start, tickets, result)
    print(answer)
    return answer


solution(tickets)
