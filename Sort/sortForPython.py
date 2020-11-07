# 파이썬의 정렬 라이브러리

# sorted

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)

print(result)


# sort

arrayTwo = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

arrayTwo.sort()
print(arrayTwo)

# key를 활용하기

arrayTrd = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


results = sorted(array, key=setting)
print(results)
