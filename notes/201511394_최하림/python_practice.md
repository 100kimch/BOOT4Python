##Python_code_study


- study source:
https://wikidocs.net/7022

####1. 변수와 데이터 타입

```
Basic: print() 하면 그냥 안에 있는거 나옴 
>>>print("Hello Wolrd")
>>>Hello World

- 문자열을 출력할 때 줄바꿈 말고 공백을 만들고 싶다면
>>>print("first", end=' ');print("second", end= ' ')
>>>first second

- 문자열 곱셈도 가능
>>>print("Hi"*3)
>>>HiHiHi

- 데이터 타입을 바꿀 때
>>>num_str = "720"
>>>num = int(num_str)

- 문자열은 배열과 같음, 배열 번지수는 0부터 시작!
>>>lang = 'python'
>>>print(lang[0])
>>>p

- 슬라이싱
>>> license_plate = "24가 2210"
>>>print(license_plate[4:])
>>>2210

>>>string = "홀짝홀짝홀짝"
>>>print(string[::2])
>>>홀홀홀

- backward print
>>> string = "PYTHON"
>>> print(string[::-1])
>>>NOHTYP

- replacing specific string
>>> phone_number = "010-1111-2222"
>>> phone_number.replace('-', ' ')
>>> 010 1111 2222

>>>string = 'abcdfe2a354a32a'
>>>string2 = string.replace('a', 'A') //변수에 넣어줘야 인식함, print(string) 하면 소문자로 출력됨(변경x)
>>>print(string2)
>>>Abcdfe2A354A32A
```
---------------------------
####2. 기본 자료구조
```
- 리스트
>>>movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
//리스트 마지막에 추가 시,
>>> movie_rank.append("배트맨")
['닥터 스트레인지', '스플릿', '럭키', '배트맨']로 저장되어 있음.

//"슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가
>>> movie_rank.insert(1, "슈퍼맨")
//index 1번 위치가 rank 0, 1 사이 = 사실 rank[1]에 새로운 데이터 입력

>>>movie_rank.remove('럭키')
// 럭키만 지워짐
>>>del movie_rank[3] 
//동일

- 리스트 저장된 데이터 개수?
>>>cook = ["1", 2", "3", "4", "5", "6", "7", "8"]
>>>print(len(cook))
>>>8

- 슬라이싱
>>>nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>print (nums[::2])
>>>1,3,5,7,9

- join() 메서드 활용
>>>interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>>print(' '.join(interest))
>>>삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

- 문자열 복사 
>>>interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
>>>interest_1 = interest_0
>>>interest_1[0] = 'Naver'
>>>print(interest_0)
>>>['Naver', 'LG전자', 'SK Hynix']

- 튜플을 리스트로 변환하기
>>>interest = ['삼성전자', 'LG전자', 'SK Hyㅑㅜㅅnix']
>>>data = list(interest)

- data unpacking
>>>my_tuple = (1, 2, 3)
>>>a, b, c = my_tuple
>>>print(a + b + c)
>>>6

- data unpacking_using * expression
>> a, b, *c = (0, 1, 2, 3, 4, 5)
>> a
0
>> b
1
>> c
[2, 3, 4]

- dictionary
>>>temp = {} //temp 라는 이름의 비어있는 딕셔너리

//example 1
이름	희망 가격
메로나	1000
폴라포	1200
빵빠레	1800

>>>icecream_price = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
>>>icecream_price['메로나'] = 1300 //메로나 가격만 수정 가능
>>>print("메로나 가격:", icecream_price['메로나']) //출력도 할 수 있고
>>>del icecream['Melona'] // 메로나 삭제할 수도 있고

//example 2
이름	가격	재고
메로나	 300    20
비비빅	 400    3
죠스바	 250    100

>>>inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
>>>print(inventory['메로나'][0], end=''); print("원")

이름	가격	재고
월드콘	500 	7

 - dictionary에 추가하려면, 
>>>inventory['월드콘'] = [500, 7] 

>>>print(icecream.keys()) //key() 매서드는 key 값만 반환 가능
>>>list(icecream.values()) // value() 매서드로 값만 반환가능
>>>sum(icecream.values()) //합도 계산가능
>>>print(icecream.update(new_product)) //일일이 다 못하니깐 

딕셔너리 / 리스트 
```

-----------------------
####3. 제어문
```
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

결과:
>>>3 //true 에서 3이 출력되고 
>>>5 //if 문 밖에서 5가 출력됨 

```
