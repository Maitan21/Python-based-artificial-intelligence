#Tutrial of Crawling using urllib

#urllib 라이브러리 input
import urllib.request

#url 과 저장할 이름 설정
url= "http://uta.pw/shodou/img/28/214.png"
savename = "test_urllip.png"

#request를 통해 파일 저장
urllib.request.urlretrieve(url,savename)
print("저장되었습니다...!")

#urlopen() 사용 -> 메모리상에 임시저장 후 오픈
mem = urllib.request.urlopen(url).read()

#파일로 저장하기 
with open("test_urlopen.png", mode="wb") as f:
    f.write(mem)
    print("Saved...!")
