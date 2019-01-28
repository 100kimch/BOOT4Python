### 기획서 작성

- 개요
  - 2018년 하반기 졸업작품 공모전에서 6조가 발표한 미세먼지 측정기와 더불어 교내 날씨 데이터를 수집하고 분석할 수 있는 디바이스 제작
  - 데이터가 중요함

#### 예산
  - 부트 재산
    - 라즈베리파이
    - R G B LED 각 1개, RGB LED(Cathode) 4개

#### 참여 인원
  - Boot4Python 프로젝트 팀 4조
    - 유재덕

#### Trend 분석
- 중국발 미세먼지에 의해 국내 정부에서는 미세먼지에 대한 구체적인 정책을 수립하고 있음
- 관련 뉴스 : 
- 다양한 분야의 IoT 디바이스 시장이 발전되고 있음에 따라 IoT 개발 경험을 가지고 있을 필요성을 느낌

#### 개발 환경 설정
- Software(사용 프로그램 및 용도)
    - VSCode : 프로그래밍 에디터
    - Git Bash : 윈도우 환경에서 Github를 사용하기 위한 터미널
    - Python 3.x : 프로그래밍 언어
- Hardware
  - Raspberry Pi : Linux 운영체제를 올릴 수 있는 디바이스

# Trouble Shoots
[Python] : 
Traceback (most recent call last):
  File "day06_sample_data.py", line 3, in <module>
    with('day06_sample_API.json') as data_file :
AttributeError: \_\_enter\_\_
 - 명령어 잘못 입력해 생긴 오류. 
 - 변경 전 : 
  ```python
  with('./day06_sample_API.json') as data_file:
  ```
 - 변경 후 : 
  ```python 
 with open('./day06_sample_API.json') as data_file:
  ```

## 개발과정
   
### UI, API, open API에 대한 이해

#### UI
>UI(User Interface)
#### API
>API(Application Programming Interface)
1. API 종류 
    - JSON : 현재 가장 자주 쓰이는 API. Python의 Dictionary 자료형과 유사한 점이 많다.
    ![JSON](https://static.goanywhere.com/images/tutorials/read-json/ExampleArray.png)
    - XML
    ![XML](https://cdn-images-1.medium.com/max/1600/1*kwUlHDYmt_TaWK7ZefEE8Q.png)

#### open API
>open API(open Application Programming Interface)

 [출처 : 한국환경정책/평가연구원](http://www.kei.re.kr/home/content/openapiintro/view.kei)
 > OpenAPI란 인터넷 이용자가 일방적으로 웹 검색 결과 및 사용자 화면 등을 제공받는 데 그치지 않고 직접 응용 프로그램과 서비스를 개발할 수 있도록 공개된 개발자를 위한 인터페이스

[공공데이터포털](https://www.data.go.kr/)

[기상청 API](http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108)

[OpenWeatherMap의 API](https://openweathermap.org/api)

본 프로젝트에선 [openweathermap](https://openweathermap.org)의 open API를 기반으로 JSON을 사용한다. 
API ID : b6907d289e10d714a6e88b30761fae22
Location : Seoul, KR