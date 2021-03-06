import requests
import json

#API 키를 지정.
apikey = "70eb0ecdfc4659fec7a181acc43a6494"

#날씨를 확인할 도시 지정
cities = ["1835327", "1853908"]

#켈빈 온도를 섭씨 온도로 변환하는 함수
k2c=lambda k: k - 273.15

#각 도시의 정보 추출하기
for cityID in cities:
    #API의 URL구성
    url =  "http://api.openweathermap.org/data/2.5/weather?id="+cityID+"&appid="+apikey
    print(url)
    #API에 요청을 보내 데이터 추출
    r = requests.get(url)
    #결과를 JSON 형식으로 변환하기 
    data = json.loads(r.text)
    #결과 출력
    print("+ 도시 =", data["name"])
    print("| 날씨 = ",data["weather"][0]["description"])
    print("| 최저 기온 = ",k2c(data["main"]["temp_min"]))
    print("| 최고 기온 = ",k2c(data["main"]["temp_max"]))
    print("| 습도 = ",data["main"]["humidity"])
    print("| 기압 = ",data["main"]["pressure"])
    print("| 풍향 = ",data["wind"]["deg"])
    print("| 풍속 = ",data["wind"]["speed"])
    print("")
