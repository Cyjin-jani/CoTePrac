# 리모컨 문제

# 컴퓨터실에서 수업 중인 정보 선생님은 냉난방기의 온도를 조절하려고 한다.

# 냉난방기가 멀리 있어서 리모컨으로 조작하려고 하는데, 리모컨의 온도 조절 버튼은 다음과 같다.

# 1) 온도를 1도 올리는 버튼

# 2) 온도를 1도 내리는 버튼

# 3) 온도를 5도 올리는 버튼

# 4) 온도를 5도 내리는 버튼

# 5) 온도를 10도 올리는 버튼

# 6) 온도를 10도 내리는 버튼

# 이와 같이 총 6개의 버튼으로 목표 온도를 조절해야 한다.

# 현재 설정 온도와 변경하고자하는 목표 온도가 주어지면 이 버튼들을 이용하여 목표 온도로 변경하고자 한다.

# 이 때 버튼 누름의 최소 횟수를 구하시오.

# 예를 들어, 7도에서 34도로 변경하는 경우,

# 7 -> 17 -> 27 -> 32 -> 33 -> 34

# 이렇게 총 5번 누르면 된다.

# 입력
# 현재 온도a 와 목표 온도b가 입력된다. ( 0 <= a , b <= 40 )

# 출력
# 최소한의 버튼 사용으로 목표온도가 되는 버튼의 횟수를 출력한다.

# 입력 예
# 7 34

# 출력 예
# 5


#내 코드 (통과)
plusButtons = [10, 5, 1]
minusButtons = [-10, -5, -1]

curTemp, targetTemp = input().split(" ")
curTemp = int(curTemp)
targetTemp = int(targetTemp)
controlTime = 0


for n in range(0, 40):
  if curTemp == targetTemp:
    break

  diff = curTemp - targetTemp
  #print("current", curTemp, "target", targetTemp)
  #print("diff", diff)

  if diff >= 0:
    a = abs(diff + minusButtons[0])
    b = abs(diff + minusButtons[1])
    c = abs(diff + minusButtons[2])
    if a > b and b > c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + minusButtons[2] 
    elif a > b and b < c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + minusButtons[1] 
    elif a < b and b < c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + minusButtons[0] 
    controlTime = controlTime + 1  
  else:
    a = abs(diff + plusButtons[0])
    b = abs(diff + plusButtons[1])
    c = abs(diff + plusButtons[2])
    if a > b and b > c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + plusButtons[2] 
    elif a > b and b < c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + plusButtons[1] 
    elif a < b and b < c:
      #print(diff, curTemp, a, b, c)
      curTemp = curTemp + plusButtons[0]
    else:
      curTemp = curTemp + plusButtons[2]   
    controlTime = controlTime + 1 

print(controlTime)


# 코드 길이:1390 byte(s) / 수행 시간:22 ms / 메모리 :33760 kb