# 정확성은 전부 패스하나, 효율성에서 탈락.

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


# def solution(participant, completion):
#     answer = ''

#     for i in range(len(participant)):
#         if participant[i] in completion:
#             completion.remove(participant[i])
#         else:
#             answer = participant[i]

#     print(answer)

#     return answer


# solution(participant, completion)


# 효율성 통과 알고리즘...

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = ''
    dic = {}

    for i in participant:
        if i not in dic:
            dic[i] = 0
        if i in dic:
            dic[i] = dic.get(i) + 1

    for c in completion:
        dic[c] = dic.get(c) - 1

    for p in participant:
        if dic[p] == 1:
            answer = p

    # print(answer)

    return answer


solution(participant, completion)
