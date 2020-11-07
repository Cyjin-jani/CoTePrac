# 프로그래머스 힙 - 디스크 컨트롤러
import heapq


jobs = [[0, 5], [2, 2], [5, 3]]
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
    print(jobs)

    while len(jobs) > 0:
        print('jobs상태', jobs)
        for i in range(len(jobs)):
            print('시작시간 판단', jobs[i][0], start)
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


# heapq사용하려던 코드 => 근데 통과가 안됨... ????
def solution2(jobs):
    answer = 0
    heap = []
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)  # 평균치를 내기 위한 디스크 총 갯수
    # heap을 만들기
    for i in range(len(jobs)):
        heapq.heappush(heap, (jobs[i][1], jobs[i]))
    # 소요시간 순으로 재정렬하기
    sorted_heap = []
    while heap:
        sorted_heap.append(heapq.heappop(heap)[1])

    while len(sorted_heap) > 0:
        print("sorted힙 상태: ", sorted_heap)
        for i in range(len(sorted_heap)):
            if sorted_heap[i][0] <= start:
                start += sorted_heap[i][1]
                answer += start - sorted_heap[i][0]
                sorted_heap.pop(i)
                break
            if i == len(sorted_heap) - 1:
                start += 1
    print("정답", answer / length)
    return answer / length


solution(jobs)
# solution2(jobs)
