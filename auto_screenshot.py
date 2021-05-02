import time
from PIL import ImageGrab

time.sleep(5) # 5초대기 : 사용자가 준비하는 시간

for i in range(1,11): #2초간격으로 10개의 이미지를 가져옴
    img = ImageGrab.grab() #현재 스크린 이미지 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장 (image.png ~ image10.png)
    time.sleep(2) #2초 단위
