# Trouble shoots
   
    1. [VSCode] Compile Error: Error description
    solution: error for compiling in VScode

## 개발 과정
   
[츨처:dydrlaks님의 medium 블로그](https://medium.com/@dydrlaks/) 
> API(Application Programming Interface, 응용 프로그램 프로그래밍 인터페이스)는 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.

[츨처:위키백과]https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9A%A9%EC%9E%90_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4) 
> UI란? 사람들이 사용하기 쉽게 해놓은 홈페이지 같은 것들. 사용자 인터페이스는 사람과 사물 또는 시스템, 특히 기계, 컴퓨터 프로그램 등 사이에서 의사소통을 할 수 있도록 일시적 또는 영구적인 접근을 목적으로 만들어진 물리적, 가상적 매개체를 뜻한다. 사용자 인터페이스는 사람들이 컴퓨터와 상호 작용하는 시스템이다.

"openAPI란? 누구나 사용할 수 있도록 공개된 API를 말하며, 개발자에게 사유 응용 소프트웨어나 웹 서비스에 프로그래밍적인 권한을 제공한다. 결론적으로 프로그래밍 방식으로 제공 받는다."

API 종류: JSON, XML

![JSON](https://www.ibm.com/developerworks/data/library/techarticle/dm-1307nosqlforjson3/DB2JSONOverview.png)

![XML](https://www.w3schools.com/xml/nodetree.gif)

JSON이 더 간단하기 때문에 본 프로젝트에서는 JSON을 사용한다.

```python
{
    "coord": {//위도,경도
        "lon": 126.98,
        "lat": 37.57
    },
    "weather": [사용할 때마다 코드 받아오기 60번 가능]
        {
            "id": 701,
            "main": "Mist",
            "description": "mist",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 278.59,
        "pressure": 1027,
        "humidity": 38,
        "temp_min": 277.15,
        "temp_max": 279.25
    },
    "visibility": 10000,
    "wind": {
        "speed": 3.6,
        "deg": 300
    },
    "clouds": {
        "all": 0
    },
    "dt": 1547794800,
    "sys": {
        "type": 1,
        "id": 8105,
        "message": 0.0074,
        "country": "KR",
        "sunrise": 1547765090,
        "sunset": 1547800815
    },
    "id": 1835848,
    "name": "Seoul",
    "cod": 200
}
```


        





        
