begin = 'hit'
target = 'log'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'lop', 'cog']


def checkWord(string1, string2):
    """문자열의 갯수가 같고 각 문자열의 문자 인덱스 비교시 1개 이하로 틀린 경우 True"""
    return True if len(string1) == len(string2) and [string1[i] == string2[i] for i in range(len(string1))].count(False) < 2 else False


def solution(begin, target, words):
    # 바꿀 수 있는 단어들 배열에 넣기
    changable = []
    answer = 0
    # target이 words안에 없으면 변환 불가.
    if not target in words:
        return 0
    # begin과 target 글자수가 다르면 0 리턴.
    if len(begin) != len(target):
        return 0

    while begin != target:
        print('지금:', begin, '타겟', target)
        for word in words:
            if checkWord(begin, word):
                if begin != word:
                    changable.append(word)
            else:
                continue
        print("현재 변화 가능한 단어들 후보", changable)
        for data in changable:
            print('현data', data)
            if data == target:
                begin = data
                answer += 1
                print(answer)
                return answer
            elif checkWord(data, target):
                changable = []
                changable.append(data)

        print("한 글자 변화시킴", begin, "에서", changable[0])
        begin = changable[0]
        words.remove(changable[0])
        answer += 1
        changable = []

    return answer


solution(begin, target, words)
