import numpy as np
import cv2
import pytesseract
# from settings import src

# 人脸识别
faceCascade = cv2.CascadeClassifier(r'C:/Users/Devotion/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# 识别眼睛
eyeCascade = cv2.CascadeClassifier(r'C:/Users/Devotion/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml')

# 开启摄像头
# cap = cv2.VideoCapture(0)
ok = True

result = []

while ok:
    img=cv2.imread("E:/001.jpg")
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    # ok, img = cap.read()
    # 转换成灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(32, 32)
    )

    # 在检测人脸的基础上检测眼睛
    for (x, y, w, h) in faces:
        fac_gray = gray[y: (y+h), x: (x+w)]
        result = []
        eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

        # 眼睛坐标的换算，将相对位置换成绝对位置
        for (ex, ey, ew, eh) in eyes:
            result.append((x+ex, y+ey, ew, eh))

    # 画矩形
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     print(x,y,x+w,y+h)
    # for (ex, ey, ew, eh) in result:
    #     cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    #     print(ex,ey,ex+ew,ey+eh)
    # cv2.imshow('video', img)
    img_std = cv2.resize(img, (748,460), interpolation=cv2.INTER_AREA) 
    # 公民身份号码
    cv2.rectangle(img_std, (60,370), (230,420), (255, 0, 0), 2)
    cv2.rectangle(img_std, (240,370), (700,420), (255, 0, 0), 2)
    # 姓名
    cv2.rectangle(img_std, (60,50), (130,100), (255, 0, 0), 2)
    cv2.rectangle(img_std, (140,50), (260,100), (255, 0, 0), 2)
    # 性别
    cv2.rectangle(img_std, (60,110), (130,160), (255, 0, 0), 2)
    cv2.rectangle(img_std, (140,110), (200,160), (255, 0, 0), 2)
    # 民族
    cv2.rectangle(img_std, (220,110), (290,160), (255, 0, 0), 2)
    cv2.rectangle(img_std, (290,110), (340,160), (255, 0, 0), 2)
    # 出生
    cv2.rectangle(img_std, (60,170), (130,220), (255, 0, 0), 2)
    # 年
    cv2.rectangle(img_std, (140,170), (220,220), (255, 0, 0), 2)
    # 月
    cv2.rectangle(img_std, (255,170), (290,220), (255, 0, 0), 2)
    # 日
    cv2.rectangle(img_std, (320,170), (360,220), (255, 0, 0), 2)
    # 住址
    cv2.rectangle(img_std, (60,230), (130,280), (255, 0, 0), 2)
    cv2.rectangle(img_std, (140,230), (460,310), (255, 0, 0), 2)
    id_num_pic=img[370:420,240:700,:]
    cv2.imshow('video', img_std)
    # content = pytesseract.image_to_string(id_num_pic)   # 解析图片
    # print(content)
    k = cv2.waitKey(1)
    if k == 27:    #按 'ESC' to quit
        break
 
cap.release()
cv2.destroyAllWindows()
# 外框（0,460）(0,748)
# 姓名（60，100）（25，100）
# 性别（120，157）（25，100）
# 民族（120，150）（195，270）
# 出生（180，212）（25，100）
# 年（175，210）（195，230）
# 月（175，210）（270，300）
# 日（175，210）（340，370）
# 住址（240，275）（25，100）
# 公民身份号码（390，425）（35，210）
# 头像（60，345）（450，690）
# (名字)（55，95）（115，270）
# 男（120，155）（115，150）
# 汉（120.155）（270，300）
# （年）（180，210）（120，190）
# （月）（180，210）（235，270）
# （日）（180，210）（300，340）
# （地址）（230，340）（120，445）
# （身份证号）（380，420）（240，655)