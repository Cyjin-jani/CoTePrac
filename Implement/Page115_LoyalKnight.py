
# coord = input()
# x = coord[0]
# y = coord[1]

# dx = [0, 0, -1, 1]
# dy = [-2, 2, 0, 0]
# move_types = [(-2, -1), (-2, 1), (-1, 2), (-1, -2),
#               (1, 2), (1, -2), (2 - 1), (2, 1)]

# counts = 0

# for move in move_types:
#     next_dx = x + move[0]
#     next_dy = y + move[1]

#     if next_dx >= 1 and next_dx <= 8 and next_dy >= 1 and next_dy <= 8:
#         count += 1

# print(counts)


#### 답안 ####

# 현재 나이트의 위치 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]


# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0  # 경우의수 카운트

for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 경우의 수 카운트를 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
