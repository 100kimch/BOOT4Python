import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup=BeautifulSoup(html,"html.parser")
for location in soup.select('location'):
        if(location.city.string== '서울'):
            for data in location.findAll('data'):
                print(data.tmef.string+"  "+data.wf.string)
            
        
        
        
       