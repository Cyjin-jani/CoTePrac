
# 결국 망한 코드임.
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# return : [ICN, JFK, HND, IAD]

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
#     "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]

# tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]

# tickets = [["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]

# tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]

tickets = [["ICN", "BBB"], ["ICN", "AAA"], ["BBB", "ICN"]]


def solution(tickets):
    answer = ['ICN']  # 무조건 인천에서 출발
    temp = []  # 재정렬 위한 임시배열
    finalLen = len(tickets) + 1
    found = False
    # now = "ICN"  # 항상 출발은 인천
    while len(answer) != finalLen:
        for i in range(len(tickets)):
            if answer[-1] == tickets[i][0]:
                temp.append(tickets[i])
        temp.sort()
        # print("temp의 상태", temp)
        if len(temp) == 1:
            answer.append(temp[0][1])
            tickets.remove(temp[0])
        else:
            if len(temp) == 0:
                # print('temp가 업슴')
                # 일단 종료조건인지 판별 후,
                # 티켓이 남아있으면,
                if len(tickets) > 0:
                    for i in tickets:
                        if i[1] == answer[0]:
                            answer.insert(0, i[0])
                            tickets.remove(i)
                            break
                # 기존의 answer를 하나씩 pop해서 지우면서 되돌아감.
            else:
                for i in range(len(temp)):
                    for j in range(len(tickets)):
                        # print('검사', temp[i][1], tickets[j][0])
                        if temp[i][1] == tickets[j][0]:
                            found = True
                            break
                    if found:
                        answer.append(temp[i][1])
                        tickets.remove(temp[i])
                        break
        temp = []
        # print("지금 남은 티켓", tickets)
        print("정답", answer)

    return answer


solution(tickets)
