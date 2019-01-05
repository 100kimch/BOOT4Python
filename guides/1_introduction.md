# 파이썬 스터디 1차시

기간: 2019. 01. 07 ~ 2019. 01. 28
장소: 건국대학교 신공학관 1203호
총원: 35명
참석 인원: 00명

## 목차

- [파이썬 스터디 1차시](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8A%A4%ED%84%B0%EB%94%94-1%EC%B0%A8%EC%8B%9C)
    - [목차](#%EB%AA%A9%EC%B0%A8)
    - [(홍보) 부트사차원 웹앱을 통한 프로젝트 생성](#%ED%99%8D%EB%B3%B4-%EB%B6%80%ED%8A%B8%EC%82%AC%EC%B0%A8%EC%9B%90-%EC%9B%B9%EC%95%B1%EC%9D%84-%ED%86%B5%ED%95%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%83%9D%EC%84%B1)
    - [프로젝트 진행방향 소개](#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A7%84%ED%96%89%EB%B0%A9%ED%96%A5-%EC%86%8C%EA%B0%9C)
        - [스터디성 프로젝트에 관한 정보](#%EC%8A%A4%ED%84%B0%EB%94%94%EC%84%B1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B4%80%ED%95%9C-%EC%A0%95%EB%B3%B4)
        - [작품제작에 관한 정보](#%EC%9E%91%ED%92%88%EC%A0%9C%EC%9E%91%EC%97%90-%EA%B4%80%ED%95%9C-%EC%A0%95%EB%B3%B4)
        - [세미나/수업에 관한 정보](#%EC%84%B8%EB%AF%B8%EB%82%98%EC%88%98%EC%97%85%EC%97%90-%EA%B4%80%ED%95%9C-%EC%A0%95%EB%B3%B4)
        - [스터디 스타일](#%EC%8A%A4%ED%84%B0%EB%94%94-%EC%8A%A4%ED%83%80%EC%9D%BC)
        - [예습 / 복습](#%EC%98%88%EC%8A%B5-%EB%B3%B5%EC%8A%B5)
        - [스터디 인원 확정 및 부원 가입](#%EC%8A%A4%ED%84%B0%EB%94%94-%EC%9D%B8%EC%9B%90-%ED%99%95%EC%A0%95-%EB%B0%8F-%EB%B6%80%EC%9B%90-%EA%B0%80%EC%9E%85)
    - [파이썬 기초](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%EC%B4%88)
        - [튜터가 프로그래밍을 공부하는 방법](#%ED%8A%9C%ED%84%B0%EA%B0%80-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%84-%EA%B3%B5%EB%B6%80%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)
        - [파이썬 철학](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B2%A0%ED%95%99)
            - [파이썬의 선 (The Zen of Python)](#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EC%84%A0-the-zen-of-python)
            - [다른 언어 철학: 자바](#%EB%8B%A4%EB%A5%B8-%EC%96%B8%EC%96%B4-%EC%B2%A0%ED%95%99-%EC%9E%90%EB%B0%94)
        - [헬로 월드 출력해보기](#%ED%97%AC%EB%A1%9C-%EC%9B%94%EB%93%9C-%EC%B6%9C%EB%A0%A5%ED%95%B4%EB%B3%B4%EA%B8%B0)
            - [Python 설치](#python-%EC%84%A4%EC%B9%98)
            - [파이썬, C 언어 헬로월드 비교](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-c-%EC%96%B8%EC%96%B4-%ED%97%AC%EB%A1%9C%EC%9B%94%EB%93%9C-%EB%B9%84%EA%B5%90)
        - [파이썬의 간략한 특징](#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-%EA%B0%84%EB%9E%B5%ED%95%9C-%ED%8A%B9%EC%A7%95)
        - [좋은 이름을 짓는 방법](#%EC%A2%8B%EC%9D%80-%EC%9D%B4%EB%A6%84%EC%9D%84-%EC%A7%93%EB%8A%94-%EB%B0%A9%EB%B2%95)
        - [파이썬 좀더 알아보기](#%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A2%80%EB%8D%94-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)
            - [Number (숫자 자료형)](#number-%EC%88%AB%EC%9E%90-%EC%9E%90%EB%A3%8C%ED%98%95)
            - [String (문자열 자료형)](#string-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%90%EB%A3%8C%ED%98%95)
            - [String Slicing (문자열 슬라이싱)](#string-slicing-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1)
            - [if, elif, else (조건문)](#if-elif-else-%EC%A1%B0%EA%B1%B4%EB%AC%B8)
            - [for, while (반복문)](#for-while-%EB%B0%98%EB%B3%B5%EB%AC%B8)
            - [List (리스트 자료형)](#list-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%A3%8C%ED%98%95)
                - [List 내장 함수들!](#list-%EB%82%B4%EC%9E%A5-%ED%95%A8%EC%88%98%EB%93%A4)
        - [기타 자료형](#%EA%B8%B0%ED%83%80-%EC%9E%90%EB%A3%8C%ED%98%95)
        - [자료형 변환](#%EC%9E%90%EB%A3%8C%ED%98%95-%EB%B3%80%ED%99%98)
    - [라즈베리 파이를 통한 파이썬 실습](#%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EB%A5%BC-%ED%86%B5%ED%95%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A4%EC%8A%B5)
        - [문제](#%EB%AC%B8%EC%A0%9C)
        - [[프로젝트] LED 구름 만들기 (1)](#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-led-%EA%B5%AC%EB%A6%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-1)
            - [기능](#%EA%B8%B0%EB%8A%A5)
            - [준비물 (4인 1조)](#%EC%A4%80%EB%B9%84%EB%AC%BC-4%EC%9D%B8-1%EC%A1%B0)
            - [참여 인원](#%EC%B0%B8%EC%97%AC-%EC%9D%B8%EC%9B%90)
            - [참고 영상](#%EC%B0%B8%EA%B3%A0-%EC%98%81%EC%83%81)
            - [실습 방법](#%EC%8B%A4%EC%8A%B5-%EB%B0%A9%EB%B2%95)
            - [유의](#%EC%9C%A0%EC%9D%98)
            - [향후 발전 방향](#%ED%96%A5%ED%9B%84-%EB%B0%9C%EC%A0%84-%EB%B0%A9%ED%96%A5)
            - [예상 시간](#%EC%98%88%EC%83%81-%EC%8B%9C%EA%B0%84)
        - [[예제] 삼거리 교차로 신호등 만들기](#%EC%98%88%EC%A0%9C-%EC%82%BC%EA%B1%B0%EB%A6%AC-%EA%B5%90%EC%B0%A8%EB%A1%9C-%EC%8B%A0%ED%98%B8%EB%93%B1-%EB%A7%8C%EB%93%A4%EA%B8%B0)
            - [문제](#%EB%AC%B8%EC%A0%9C)
            - [해설](#%ED%95%B4%EC%84%A4)
        - [[예제] 7-세그먼트를 이용한 숫자 표현하기](#%EC%98%88%EC%A0%9C-7-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%88%AB%EC%9E%90-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0)

## (홍보) 부트사차원 웹앱을 통한 프로젝트 생성

[부트사차원 신규사이트: boot4dim.com](https://boot4dim.com)
새롭게 만든 부트사차원 웹앱에 프로젝트 추가/관리 기능이 있으니 본인이 하고싶은 프로젝트 있으면 언제든지 프로젝트 만들어서 진행하면 됩니다.

- 주요 기능
  1. 프로젝트 페이지 생성 및 관리를 통해 자연스럽게 프로젝트 진행방법을 배울 수 있습니다.
  2. 필요한 예산을 사이트 내에서 지원 요청하고 받을 수 있습니다.
  3. 부트사차원 회원 누구나 진행된 모든 프로젝트를 열람할 수 있습니다.
  4. 향후 개인이 참여한 프로젝트를 토대로 개인 포트폴리오를 소프트 카피 형식으로 받아볼 수 있습니다.

## 프로젝트 진행방향 소개

- 이름: Boot4Python
- 목표(이 스터디를 공부하게 된다면)
  - 코딩 입문자로서 어떻게 소프트웨어 개발 공부를 해야하는지 개인 로드맵을 짤 수 있습니다.
  - 프로그래밍 언어 파이썬 및 간단한 알고리즘을 배웁니다.
  - 캔들차트 그리기, 날씨정보 출력하기 등 파이썬 라이브러리를 이용한 파이썬 활용 방법을 배웁니다.
  - 다수의 작품 제작 실습을 통해 프로젝트 진행 방법을 배웁니다.
  - 꾸준한 기록을 통해 자신의 포트폴리오를 남기고, 부트사차원 후배에게 지식을 공유합니다.
- 유형: 스터디성 프로젝트 / 수업
- 분야: 소프트웨어 / 코딩
- 기간: 3주 총 10회 각 3시간
  - 1주차: 월 (목) 금
  - 2~3주차 월 수 금
  - 4주차 월 (목)
- 팀장: 김지형
- 인원: 35명 (2주차 이후 20여명)
- 장소: 신공학관 1203호

### 스터디성 프로젝트에 관한 정보

- 주제: 파이썬, 라즈베리파이
- 모임: 3주 총 10회
- 튜터: 김지형

### 작품제작에 관한 정보

- 해당사항 없음

### 세미나/수업에 관한 정보

- 수정 요함

### 스터디 스타일

- 수업, 스터디라 생각하지 않고 재미있게 놀다 가는 모임이라고 생각하기를 바라는 마음입니다.
- 2시간 수업, 1시간 실습으로 잡았으나, 정해진 시간 신경쓰지 않고 더 하고싶은 사람은 자유롭게 진행할 수 있습니다.
- 스터디 중간에 쉬고싶으면 쉬어도 되고, 놀고싶으면 노세요
- 수업중에는 최대한 많이 물어보세요.

### 예습 / 복습

- 프로젝트 페이지 > 개인노트를 자주 이용하세요.
- 매일 하나씩 개인노트에 배운 내용을 정리해서 저장해두세요.
- 예습은 필요하지 않습니다.
- 배운 내용을 토대로 응용할 수 있는 방법을 최대한 많이 찾아보시고, 그에 대한 구현 방법을 튜터한테 물어보세요.
- 마크다운 글 작성 요령은 추후 소개하겠습니다.

### 스터디 인원 확정 및 부원 가입

- 1주차는 출석체크를 하지 않습니다.
- 1주차 두번의 수업을 해보시고 자신의 이익에 맞게 열정적으로 참여하실 분만 2주차 이후 수업을 계속 들어주세요.
- 2주차 수업부터 부트사차원 회비를 내신분에 한하여 수업이 진행되며, 출결 관리를 합니다.
- 5000원의 스터디비를 받고, 성실히 참여하신 분은 스터디비를 돌려드립니다. (예정, 의견 수렴)

## 파이썬 기초

### 튜터가 프로그래밍을 공부하는 방법

- 기존 학교에서 가르쳐주는 프로그래밍 수업은 int 자료형의 크기 범위, 수많은 내장 함수 등등 불필요하게 많은 내용을 알려주지만, 튜터 본인은 처음에 그런 식의 프로그래밍 언어 습득은 학생의 흥미를 떨어뜨리는 안 좋은 수업 방법이라 생각합니다.
- 세세한 특성에 신경쓰지 마세요. 구글링하면 그런 내용은 다 나옵니다.
- 그 대신, 언어를 배우는 목적을 명확히 해주세요. 영어, 한국어도 의사를 표현하는 데 쓰이는 도구인 것처럼, 파이썬 역시 컴퓨터가 기능을 수행하는 데 쓰는 도구일 뿐입니다. '나는 파이썬을 이용해 미세먼지 측정기를 만들어야지'라는 생각 하나씩 가지고 있으면 좋습니다.

### 파이썬 철학

- 오늘날 인간이 쓰는 언어가 다양한 이유? => 역사적, 지리적 요인, 그러나 하는 역할은 유사하다.
- 오늘날 프로그래밍 언어가 다양한 이유? => 하는 역할이 다소 다르다.
- 2018 프로그래밍 언어 순위: Java, C, C++, Python..
- 2019년도에 Python이 3위로 올라서면서 파이썬의 인기는 꾸준하게 상승하고 있음을 알 수 있다.
- 파이썬이 하는 역할은 무엇이고, 어떤 목적으로 만들어졌을까? => 철학을 알자
- 파이썬 콘솔에서 다음을 쳐보자.

  ```python
  import this
  ```

#### 파이썬의 선 (The Zen of Python)

[위키독스](https://wikidocs.net/7907)

```text
Beautiful is better than ugly. 아름다움이 추한 것보다 낫다.

Explicit is better than implicit. 명확함이 함축된 것보다 낫다.

Simple is better than complex. 단순함이 복잡한 것보다 낫다.

Complex is better than complicated. 복잡함이 난해한 것보다 낫다.

Flat is better than nested. 단조로움이 중접된 것보다 낫다.

Sparse is better than dense. 여유로움이 밀집된 것보다 낫다.

Readability counts. 가독성은 중요하다.

Special cases aren't special enough to break the rules. 규칙을 깨야할 정도로 특별한 경우란 없다. Although practicality beats purity. 비록 실용성이 이상을 능가한다 하더라도.

Errors should never pass silently. 오류는 결코 조용히 지나가지 않는다. Unless explicitly silenced. 알고도 침묵하지 않는 한.

In the face of ambiguity, refuse the temptation to guess. 모호함을 마주하고 추측하려는 유혹을 거절하라. There should be one-- and preferably only one --obvious way to do it. 문제를 해결할 하나의 - 바람직하고 유일한 - 명백한 방법이 있을 것이다. Although that way may not be obvious at first unless you're Dutch. 비록 당신이 우둔해서 처음에는 명백해 보이지 않을 수도 있겠지만.

Now is better than never. 지금 하는 것이 전혀 안하는 것보다 낫다. Although never is often better than right now. 비록 하지않는 것이 지금 하는 것보다 나을 때도 있지만.

If the implementation is hard to explain, it's a bad idea. 설명하기 어려운 구현이라면 좋은 아이디어가 아니다. If the implementation is easy to explain, it may be a good idea. 쉽게 설명할 수 있는 구현이라면 좋은 아이디어일 수 있다. Namespaces are one honking great idea -- let's do more of those! 네임스페이스는 정말 대단한 아이디어다. -- 자주 사용하자!
```

- 나 이런것도 안다 자랑하자
- 간단하고, 단순하고, 읽기 좋은 프로그래밍 언어를 만들어보자!

#### 다른 언어 철학: 자바

[자바의 철학](https://wikidocs.net/7907)

### 헬로 월드 출력해보기

#### Python 설치

[다양한 운영체제에서 파이썬 설치법](http://pythonstudy.xyz/python/article/2-Python-%EC%84%A4%EC%B9%98)

- 방법 1 (윈도우 10)
  - Microsoft 앱스토어에서 Ubuntu Linux를 다운받는다.
- 방법 2 (윈도우 전체)
  1. 브라우저에서 [파이썬 공식사이트](https://www.python.org/downloads/) 방문
  1. 윈도우즈용 Python 3 버젼 다운 받아 설치
  1. 설치마법사에서 Custom 설치를 선택, 옵션에서 Python 경로 환경변수에 추가를 선택하면 편리

#### 파이썬, C 언어 헬로월드 비교

```c
// C언어 예제 1
#include <stdio.h>
int main(int argc, char * argv[]) {
    printf("Hello World!\n");
    return 0;
}
```

```python
# 파이썬 예제 1
print("Hello World!")
```

```c
// C언어 예제 2
#include <stdio.h>
void main()
{
    char *s1 = "Hello World!";
    for (int i = 0; i < 5; i++)
    {
        printf("%s\n", s1);
    }
    return 0;
}
```

```python
# 파이썬 예제 2
str = "Hello World!"
for i in range(5):
    print("Hello World!")
```

```c
// C언어 예제 3
#include <stdio.h>
#include <math.h>

int main() {
    double num = 0, squareRoot;

    for( num; num < 5, ++num) {
        squareRoot = sqrt(num);
        printf("%lf의 제곱근은 %lf 입니다.", num, squareRoot);
    }
    return 0;
}
```

```python
# 파이썬 예제 3
import math
for i in range(9):
    n = math.sqrt(i)
    print(str(i) + ' 의 제곱근은 ' + str(n) + '입니다.')
```

- 파이썬의 코드를 보고 있노라면 C 언어가 무지 복잡해보인다.
- c언어의 include와 파이썬의 import가 유사하다는 것을 확인할 수 있다.
- c언어에서는 main 함수가 있지만, 인터프리터 기반의 파이썬은 메인 함수가 없다.
- c언어에서는 중괄호로 포함관계를 구분짓지만, 파이썬은 들여쓰기, 콜론으로 구분한다. (몇칸인지보다 스페이스 수가 일치해야 한다.)
- 세미콜론이 없다.
- for 문의 조건 식이 상이하다.
- 파이썬은 자료형 선언이 없다. 그러나 문자열, 숫자 등에 구분이 있어 프린트를 해줄 때 변환작업이 필요하다. (str()함수 보기)

### 파이썬의 간략한 특징

[Python-시작하기](http://pythonstudy.xyz/python/article/3-Python-시작하기)

- 파이썬 셸, 또는 대화형 인터프리터라는 콘솔 프로그램이 존재한다.
- C언어와 달리 파이썬은 이 셸을 통해 코드 한줄 단위로 코드 실행을 가능하게 해준다.
- 여기서 처음 나오는 >>>는 파이썬 인터프리터의 프롬프트로서, 사용자의 입력을 기다리는 표시이다. 다른 콘솔 프로그램의 >, \$, # 등도 같은 역할을 하는 것을 볼 수 있다.
- C언어와 같이 파일 단위로 실행시켜주는 방법도 존재한다.

```bash
nano hello.py
```

- 위 코드로 나노 에디터를 실행시킬 수 있으며 나노 에디터 안에 다음을 입력한다.

```python
print("Hello World")
```

- Ctrl+X, Y, Enter를 차례대로 눌러준다.
- python ./hello.py를 통해 파이썬을 실행해준다.

- 새 파일을 열어 다음을 입력한다.

```python
import math
for i in range(9):
    n = math.sqrt(i)
    print(str(i) + ' 의 제곱근은 ' + str(n) + '입니다.')
```

- 한글식 언어로 해석해보자.

```text
수학을 가져오기
i라는 변수를 (9)번 반복하는데:
    n = 수학.제곱근(i)
    (str(i) + ' 의 제곱근은 ' + str(n) + '입니다.')를 출력
```

- 한국어를 쓰는데 영어를 쓰다보니 어렵게 느껴지는 부분이 있다. 파이썬이 영문법과 유사한 구조라는 것을 알고 영어 문법에 맞게 적어보려 노력하자.
- 콤마 하나, 콜론 하나에 신경쓰자
- 컴퓨터는 개새끼다. 한가지 일만 할 수 있는 단순한 존재이며, 두가지 이상 하려면 한개씩 시켜야 한다.
- import 라이브러리를 표준말, 부산사투리 등으로 생각하자.

### 좋은 이름을 짓는 방법

(https://medium.com/@kkweon/%ED%8C%8C%EC%9D%B4%EC%8D%AC-doc-%EC%8A%A4%ED%83%80%EC%9D%BC-%EA%B0%80%EC%9D%B4%EB%93%9C%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC-b6d27cd0a27c)

- 모든 프로젝트 개발에는 코딩 스타일 가이드가 존재한다. 규칙성과 일관성, 직관성을 위해 지켜주자.

  - PEP8
  - 모듈의 이름은 only 소문자
  - class는 camelCase
  - 함수의 이름은 snake_case
  - 들여쓰기는 스페이스 4칸

- 본 스터디에서는 다음과 같이 정한다.

  - 변수/함수의 이름은 camelCase
  - 들여쓰기는 스페이스 4칸

### 파이썬 좀더 알아보기

[기초 문법 1](https://blog.leop0ld.org/posts/python-basic-grammar1/)
[기초 문법 2](https://blog.leop0ld.org/posts/python-basic-grammar2/)

#### Number (숫자 자료형)

```python
# 기본적인 사칙연산
print(5 + 6)   # 11
print(5 - 2)   # 3
print(3 * 8)   # 24
print(3 ** 3)  # 27 제곱
print(8 / 2)   # 4.0 float형
print(8 // 2)  # 4 int형
print(8 % 3)   # 2 나머지
```

#### String (문자열 자료형)

```python
test = "Hello World!"
print(test)  # Hello World!

test = 'Hello!'
print(test)  # Hello!

test = 'I don\'t need Coke!'
print(test)  # I don't need Coke!

test = "I don't need Coke!"
print(test)  # I don't need Coke!
```

- C언어와 같이 test = ['H', 'e', 'l', 'l', ....] 방식으로 배열이 형성되는 것을 알아두자.

#### String Slicing (문자열 슬라이싱)

```python
test_str = 'Leopold'

print(test_str[0])   # L
print(test_str[1])   # e
print(test_str[-1])  # d
print(test_str[-2])  # l
```

- List의 인덱스 부분에 음수를 넣어서 오른쪽부터 가져올 수 있습니다.
- 주의할 점은 음수로 인덱싱할 경우에는 0부터 시작이 아니라 1부터 시작합니다.

```python
print(test_str[2:5])  # opo
print(test_str[3:6])  # pol
print(test_str[:5])   # Leopo
print(test_str[3:])   # pold
```

- 이렇게 범위를 인덱스로 지정해서 호출하는 것도 가능합니다.
- 주의할 점은 콜론 앞의 숫자는 포함되지만 뒤의 숫자는 포함되지 않습니다.
- 시작지점을 지정하지 않으면 처음부터 콜론 뒷 부분 숫자의 인덱스까지 출력하고, 끝지점을 지정하지 않으면 콜론 앞 부분 숫자부터 끝까지 출력합니다.

#### if, elif, else (조건문)

```python
name = 'Leopold'

if name is 'Myungseo':
    print('Hello Myungseo')
elif name is 'Kang':
    print('Hello Kang!')
else:
    print('Hello Everyone!')
```

- C언어에서는 else if 인 부분이 elif로 바뀌었다는점 유념해주세요.

#### for, while (반복문)

for, while 문은 반복문입니다. 말그대로 반복시키기 위한 구문입니다. for문의 기본 구조는 아래와 같습니다.

```python
test = [1, 2, 3, 4, 5]

for i in test:
    print(i)
    '''
    1
    2
    3
    4
    5
    '''

```

다음과 같이 i 부분에는 변수, test 부분에는 List나 Tuple 혹은 String 같은 반복가능한 변수가 옵니다. 그 다음에는 하고싶은 코드를 적으면 됩니다. 그리고 아래와 같이도 사용할 수 있습니다.

```python
test = [(1, 2), (3, 4)]

for (i, j) in test:
    print(i+j)
    '''
    3
    7
    '''
```

이렇게도 사용이 가능합니다. C언어의 for문보다는 간편하게 사용할 수 있는 것 같습니다.

```python
for i in range(0, 10):
    print(i)
```

range 객체를 이용해서 쉽게 for문을 만들수도 있습니다.
간단하게 List 내장 함수와 for문을 이용한 예제를 보겠습니다.

```python
test_list = [1, 2, 3, 4, 5]
result = []

for num in test_list:
    result.append(num*3)

print(result)  # [3, 6, 9, 12, 15]
```

이런 코드를 아래와 같이 요약할 수 있습니다

```python
test_list = [1, 2, 3, 4, 5]

result = [num * 3 for in test_list]

print(result)  # [3, 6, 9, 12, 15]
```

이렇게 for문을 알아보았습니다.

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

## 라즈베리 파이를 통한 파이썬 실습

- Raspberry_pi 1주차.pdf 참고
- 2.7 버전을 이용하기 때문에 문법이 다소 상이하다.

```python
# import RPi.GPIO로 코딩을 해보는 연습도 해보자
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print "LED를 출력으로 설정합니다."
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)
GPIO.output(23, True)
time.sleep(1)
GPIO.output(23, False)
raw_input('enter 키를 눌러 종료하십시오.') GPIO.cleanup()
```

### 문제

1. 1개의 LED를 이용하여 10초, 5초, 2.5초 ... 간 깜빡꺼리기를 구현한다. 0.1초 이내의 간격이 될 때 프로그램을 종료한다.
2. 3개의 LED를 이용하여 0.5초 간격으로 왼쪽에서 오른쪽으로 흐르는 LED를 구현한다.

### [프로젝트] LED 구름 만들기 (1)

#### 기능

라즈베리파이 기반 led 키고 끄기

#### 준비물 (4인 1조)

라즈베리파이 1세트, sd 카드 1개, 충전 케이블 1개, 220 Ohm 저항 8개, 110 Ohm 4개, led R G B 각 1개, rgb LED(cathode) 4개, 빵판, 점퍼케이블, 장식용 솜, 꾸미기 재료

#### 참여 인원

4인 1조 총 8 ~ 10팀

#### 참고 영상

(https://m.facebook.com/groups/818939704832393?view=permalink&id=2094381107288240)

#### 실습 방법

1. 4인 1조가 되어 프로젝트를 시작한다.
2. 프로젝트 준비를 위한 몇가지 작업을 진행한다.

   - 1팀: 구름을 만들 수 있는 꾸미기 재료를 다이소가서 사오기
   - 1팀: 마실 음료수 사오기
   - 2팀: 동방 소파 설치 도와주기 및 동방에서 110Ohm 40개, 220Ohm 80개, 니퍼, 스트립퍼 등 구름 만들기 준비물 가져오기, 종이컵 및 물티슈 가져오기
   - 6팀: 라즈베리파이 OS설치 및 환경설정
   - 질문있는 회원은 따로 질문받기

3. 팀 역할분담은 이름맞추기 게임으로 한다.

#### 유의

- R 노드에는 110Ohm의 저항을 이용하며, G, B 노드에는 220Ohm의 저항을 이용한다.

#### 향후 발전 방향

- PWM으로 더욱 다채로운 색 구현하기
- git 이용하여 원격으로 설정 변경하기
- 날씨 API를 받아와서 날씨 정보에 따라 색 변하게 하기
- 3D 프린팅을 이용하여 휴대용으로 만들기

#### 예상 시간

- 팀 구성 및 개인 환경설정: 10분
- 팀별 프로젝트 준비: 40분
- 제작: 10분

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

```C
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
