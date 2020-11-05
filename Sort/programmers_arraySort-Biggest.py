# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


numbers = [2, 10, 6]
# return 6210

# 다른 사람의 풀이....
# 문제의 numbers의 원소는 0 이상 1,000 이하입니다. 라는 조건을 통해서 numbers.sort(key=lambda x" x*3, reverse = True)를 해서 정렬
# [6, 10, 2]을 예시로 들면, numbers.sort(key=lambda x" x*3, reverse = True)를 하면,
# [666, 101010, 222]가 되고 이를 정렬하면, [666, 222, 101010]이 되어서 결과적으로 [6, 2, 10]의 순서가 된다.
# 위와 같이 정렬되는 이유는 박상희님의 댓글에 따르면 "문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다."
# 즉, 앞자리가 큰 6 -> 2 -> 1순으로 정렬되어서 위와 같은 결과를 얻게 된 것입니다.


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    # print(answer)
    return answer


solution(numbers)
