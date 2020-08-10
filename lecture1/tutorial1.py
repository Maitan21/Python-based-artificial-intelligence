#Tutrial of Crawling using urllib

#urllib 라이브러리 input
import urllib.request

#url 과 저장할 이름 설정
url= "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#request를 통해 파일 저장
urllib.request.urlretrieve(url,savename)
print("저장되었습니다...!")