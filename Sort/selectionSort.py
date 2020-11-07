# 선택정렬 알고리즘
# 가장 작은 데이터를 선택해 맨 앞으로.
# 그 다음 작은 데이터를 선택해 앞에서 2번째로.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)
