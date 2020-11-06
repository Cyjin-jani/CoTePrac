# 프로그래머스 힙 - 디스크 컨트롤러
# import heapq
# heap = []

jobs = [[0, 3], [4, 3], [8, 3]]
# [[0, 3], [1, 9], [2, 6]] 9
# [[0, 3], [4, 3], [8, 3]] 3

# [[0, 5], [6, 1], [6, 2]] 3
# [[0, 5], [6, 2], [6, 1]] 3
# [[0, 5], [2, 2], [5, 3]] 5
# [[0, 5], [2, 2], [4, 2]] 5


def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)  # 평균치를 내기 위한 디스크 총 갯수

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬
    # print(jobs)

    while len(jobs) > 0:
        print('jobs상태', jobs)
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                print("종료시간, 시작시간", start, jobs[i][0])
                print('총걸린시간(누적)', answer)
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 추가함. (이 부분이 어려웠음)
            elif i == len(jobs) - 1:
                start += 1

    print("답: ", answer // length)
    return answer // length


solution(jobs)
