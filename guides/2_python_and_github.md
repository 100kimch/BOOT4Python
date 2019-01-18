# 부트 SW 스터디 2차시

- 일시: 2019. 01. 09 오후 3시 ~ 오후 6시
- 참석 인원: 35명
- 튜터: 김지형(100kimch@naver.com)

## 파이썬 기초 (2차시)

### 파이썬 좀더 알아보기

#### List (리스트 자료형)

- List는 배열이라고 생각하면 편합니다.

```python
a = [] # a = list()와 동일
b = [1, 3, 5]
c = ['Leopold', 'Myungseo', 'Kang', 'L3opold7']
d = [7, 9, ['Myungseo', 'L3opold7']]
```

- List 안에는 여러가지 자료형을 담을 수 있습니다.
- List에도 Slicing String에서 말한 것들을 적용할 수 있습니다.

```python
print(b[-1])     # 5
print(c[-2])     # Kang
print(d[-1][0])  # Myungseo
```

- 이중 List에서 인덱싱은 다음과 같이 할 수 있습니다.

```python
# List 값 수정
test = [1, 2, 3, 4, 5]
test[3] = 6

print(test)  # [1, 2, 3, 6, 5]
```

이렇게 인덱스를 지정해서 직접 값을 바꿔줄 수 있습니다.

```python
# List 연속된 값으로 변경
test = [1, 2, 3, 4, 5]
test[2:3] = ['a', 'b', 'c']

print(test)  # [1, 2, 'a', 'b', 'c', '4', '5']
```

2이상 3미만의 인덱스 부분에 a,b,c List를 변경해주는 것입니다.

```python
# List 요소 삭제
test = ['a', 'b', 'c', 'd', 'e']
test[2:4] = []

print(test)  # ['a', 'b', 'e']
# del 함수 사용
test = ['a', 'b', 'c', 'd', 'e']
del test[2]

print(test)  # ['a', 'b', 'd', 'e']
```

del 함수를 사용해서 삭제할 수도 있습니다.

```python
test = ['a', 'b', 'c', 'd', 'e']
del test[2:4]

print(test)  # ['a', 'b', 'e']
```

마찬가지로 인덱스를 범위로 지정하는 것 또한 가능합니다.

##### List 내장 함수들!

```python
test = [1, 2]
test.append(3)  # 맨 뒤에 값 추가
print(test)  # [1, 2, 3]
```

append(x) 함수는 인자를 1개밖에 받지 않기 때문에 여러개의 인자를 넘겨줄 경우 에러가 납니다.

```python
test = [3, 1, 2, 5, 4]
test.sort()
print(test)  # [1, 2, 3, 4, 5]

test.sort(reverse=True)
print(test)  # [5, 4, 3, 2, 1]
```

sort() 함수는 List를 자동으로 정렬해줍니다. 역순으로 정렬하기 위해서는 sort 함수에 reverse 옵션을 True로 설정해주면 됩니다.

```python
test = [3, 1, 2]
test.reverse()
print(test)  # [2, 1, 3]
```

reverse() 함수는 현재의 List를 역순으로 뒤집어 줍니다. 정렬은 하지 않고 현재의 List를 역순으로 뒤집어 줍니다.

```python
test = [1, 2, 3, 4, 5]
print(test.index(3))  # 2
print(test.index(5))  # 4
```

index(x) 함수는 x 라는 값이 있는 경우 , x 의 인덱스를 반환해주는 함수입니다.

```python
test = [1, 2, 3, 4, 5]
test.insert(0, 6)
print(test)  # [6, 1, 2, 3, 4, 5]
```

insert(x, y) 함수는 x 위치에 y 라는 값을 삽입해주는 함수입니다.

```python
test = [1, 2, 3, 4, 3]
test.remove(3)
print(test)  # [1, 2, 4, 3]
```

remove(x) 함수는 첫 번째로 나오는 x 라는 값을 List에서 삭제해주는 함수입니다. 보시다시피 뒷부분에 있는 3은 삭제되지 않았습니다.

```python
test = [1, 2, 3]
print(test.pop())  # 3
print(test)        # [1, 2]
```

pop() 함수는 List의 가장 마지막 인덱스의 값을 반환해주고 그 값을 삭제해주는 함수입니다. 위의 예제에서 굳이 3이라는 값이 필요없을 경우에는 print() 함수를 빼도 상관없습니다.

```python
test = [1, 2, 3, 1, 1]
print(test.count(1))  # 3
```

count(x) 함수는 x 라는 값이 List 안에 몇 개나 있는지 반환해주는 함수입니다.

```python
test = [1, 2, 3]
test.extend([4, 5, 6])
print(test)  # [1, 2, 3, 4, 5, 6]
```

extend(x) 함수는 x 부분에 List를 받아서 원래의 List와 병합시켜주는 함수입니다.
List에서는 위와 같은 내장 함수들을 사용할 수 있습니다. 여기에 더해서 len() 함수로 List 값들의 개수를 얻을 수 있습니다.

### 기타 자료형

- Tuple, Dictionary, Set 자료형은 다음에 공부하기로 한다.

### 자료형 변환

- Raspberry_pi 1주차.pdf 20/44 페이지 참고
- int(), float(), str(), list() 등을 이용해줄 수 있다.

### [예제] 삼거리 교차로 신호등 만들기

#### 문제

건국대학교 후문 삼거리의 신호등이 밤새 술먹다 꺵판친 인원이에 의해 부서졌습니다. 신호등을 고칠 겸 새롭게 신호체계를 개편하려고 합니다. 다음과 같이 신호체계를 구성하여 라즈베리파이와 LED로 신호체계를 구현해 주세요.

1. T자 교차로에서 왼쪽에서 오는 차로의 신호등을 1번, 오른쪽 신호등을 2번, 아래쪽 신호등을 3번이라 칭한다. 그리고 통상 횡단보도마다 2개의 신호등이 존재하지만, 두 신호등이 같은 패턴을 가지므로 횡단보도의 신호등은 하나만 구현하기로 한다. 오른쪽 횡단보도의 신호등을 4번, 아래쪽 횡단보도의 신호등을 5번으로 칭한다.
1. 신호등의 색은 다음과 같이 정한다.
   | 신호 | 색상 |
   | --- | --- |
   | 정지 | Red |
   | 주의 | Yellow |
   | 직진 | Green |
   | 좌회전 | Blue |
1. 각 신호등은 다음과 같은 신호를 보낼 수 있으며, 표시 순서를 바꾸지 않는다.
   | 신호등 | 신호 |
   | --- | --- |
   | 1번 | 정지, 주의, 직진 |
   | 2번 | 정지, 주의, 좌회전, 직진 |
   | 3번 | 정지, 주의, 좌회전 |
   | 4번 | 정지, 직진 |
   | 5번 | 정지, 직진 |
1. 각 신호등은 하나의 신호를 보내는 것을 원칙으로 하나, 2번 신호등의 경우 좌회전 신호일 때는 좌회전 신호와 함께 정지 신호를 같이 표시해주어야 한다.
1. 횡단보도 신호등은 직진 신호 시 깜빡거려야 한다. 0.5초 간격으로 켜지고 꺼지기를 반복한다.
1. 먼저 모든 신호등이 정지 신호를 보낸다. 1초간 유지한다.
1. 1번과 2번 신호등이 직진 신호를 보낸다. 5번 횡단보도 신호등 역시 직진신호를 보낸다. 10초간 유지한다.
1. 1번과 2번 신호등이 주의 신호를 보내며, 5번 신호등은 정지 신호를 보낸다. 3초간 유지한다.
1. 1번 신호등은 정지, 2번 신호등은 좌회전 신호를 보낸다. 5초간 유지한다.
1. 2번 신호등이 주의 신호를 보낸다. 3초간 유지한다.
1. 2번 신호등이 정지 신호를 보내며 3번 신호등이 좌회전 신호를 보낸다. 4번 신호등은 직진 신호를 보낸다. 5초간 유지한다.
1. 3번 신호등이 주의 신호를 보내며, 4번 신호등은 정지 신호를 보낸다. 3초간 유지한다.
1. 6번 과정으로 돌아가 반복한다.

#### 해설

1. 필요한 LED, 저항 개수를 파악한다. R5, G4, B2, Y3
1. RGB LED를 이용하여 노란색을 구현하려 할 경우, R과 G를 같이 켜주면 된다.
1. 다음과 같이 코드를 작성한다.

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "LED를 출력으로 설정합니다."

lamps = [[2, 3, 4], [17, 27, 22, 10], [9, 11, 5], [6, 13], [19, 26]]

def reset_all(lamps):
    GPIO.cleanup()
    for lamp in lamps:
        for (key, value) in enumerate(lamp):
            GPIO.setup(i, GPIO.OUT)
            if key == 0:
                GPIO.output(value, True)
            else:
                GPIO.output(value, False)

def reset_lamps(lamp):
    for i in lamp:
        GPIO.output(i, False)

# mode = int in {'정지': 0, '주의': 1, '좌회전': 2, '직진': 3}
def set_color(mode, lamp):
    reset_lamps(lamp)
    if mode == 0:
        GPIO.output(lamp[0], True)
    else:
        length = len(lamp)
        if length == 2 and mode == 4:
            GPIO.output(lamp[1], True)
        elif length == 3:
            if mode == 1:
                GPIO.output(lamp[1], True)
            elif mode == 2 or mode == 3:
                GPIO.output(lamp[2], True)
        else:
            GPIO.output(lamp[mode], True)

reset_all(lamps)
time.sleep(1)
set_color(4, lamps[0])
set_color(4, lamps[1])
set_color(4, lamps[2])

time.sleep(1)
GPIO.output(23, False)
raw_input('press enter to exit program') GPIO.cleanup()
```

### [예제] 7-세그먼트를 이용한 숫자 표현하기

[C언어 예제](https://kocoafab.cc/tutorial/view/351)

```c
/*
 제목		: 7세그먼트로 숫자 표시하기
 내용		: 7세그먼트를 사용하여 0부터 9까지 숫자를 표시해 봅시다.
 */

// 7세그먼트는 총 8개의 LED로 구성이 되어 있습니다.
// 본 예제에서는 공통 애노드(Common Anode) 타입의 7세그먼트를 사용함으로,
// 켜고자 하는 LED의 핀에 LOW(0) 값을 보내도록 설정합니다.
// 반대로, 공통 캐소드(Common Cathode) 타입을 사용할 경우, HIGH(1) 값으로 설정합니다.
// 7세그먼트 각각 LED에 핀을 할당합니다. {A, B, C, D, E, F, G, H}
int segmentLEDs[] = {2, 3, 4, 5, 6, 7, 8, 9};
// 지정된 LED 개수
int segmentLEDsNum = 8;

// 각 숫자에 대한 LED 설정 값을 정의합니다.
// 숫자에 매칭되는 LED의 로직레벨을 LOW(0) 상태로 설정합니다.
int digitForNum[10][8] = {
	{0, 0, 0, 0, 0, 0, 1, 1}, //0
	{1, 0, 0, 1, 1, 1, 1, 1}, //1
	{0, 0, 1, 0, 0, 1, 0, 1}, //2
	{0, 0, 0, 0, 1, 1, 0, 1}, //3
	{1, 0, 0, 1, 1, 0, 0, 1}, //4
	{0, 1, 0, 0, 1, 0, 0, 1}, //5
	{0, 1, 0, 0, 0, 0, 0, 1}, //6
	{0, 0, 0, 1, 1, 1, 1, 1}, //7
	{0, 0, 0, 0, 0, 0, 0, 1}, //8
	{0, 0, 0, 0, 1, 0, 0, 1}  //9
};

// 실행시 가장 먼저 호출되는 함수이며, 최초 1회만 실행됩니다.
// 변수를 선언하거나 초기화를 위한 코드를 포함합니다.
void setup() {
	// 7세그먼트 각각 LED에 연결된 핀을 OUTPUT으로 설정합니다.
	for (int i = 0 ; i < segmentLEDsNum ; i++) {
		pinMode(segmentLEDs[i], OUTPUT);
	}
}

// setup() 함수가 호출된 이후, loop() 함수가 호출되며,
// 블록 안의 코드를 무한히 반복 실행됩니다.
void loop() {
	// 0부터 9까지 숫자를 순서대로 표시합니다.
	for (int i = 0 ; i < 10 ; i++) {
		// 각 숫자에 대한 각각 LED의 로직레벨을 설정합니다.
		for (int j = 0 ; j < segmentLEDsNum ; j++) {
			digitalWrite(segmentLEDs[j], digitForNum[i][j]);
		}
		// 1초 동안 대기합니다.
		delay(1000);
	}
}
```
