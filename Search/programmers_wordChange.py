begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']


def checkWord(string1, string2):
    """문자열의 갯수가 같고 각 문자열의 문자 인덱스 비교시 1개 이하로 틀린 경우 True"""
    return True if len(string1) == len(string2) and [string1[i] == string2[i] for i in range(len(string1))].count(False) < 2 else False


def solution(begin, target, words):
    answer = 0
    # target이 words안에 없으면 변환 불가.
    if not target in words:
        return 0
    # begin과 target 글자수가 다르면 0 리턴.
    if len(begin) != len(target):
        return 0

    while begin != target:
        for i, word in enumerate(words):
            if checkWord(begin, word):
                begin = word
                answer += 1
                words.pop(i)
                print('바꿈', begin)
                break

    return answer


solution(begin, target, words)
