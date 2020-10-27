import numpy as np
import cv2
import pytesseract
import time
import csv
# from settings import src
def cut_img(img,x1,y1,x2,y2):
    
    ret, binary_img = cv2.threshold(img[y1:y2,x1:x2], 147, 255, cv2.THRESH_BINARY)
    return binary_img
    # return img[y1:y2,x1:x2]
def ocr(img):
    content = pytesseract.image_to_string(img,lang='chi_sim',config='--psm 6 --oem 3')   # 解析图片
    return content.strip().replace(' ', '').replace('\n', '').replace('\r', '')
# 人脸识别
# faceCascade = cv2.CascadeClassifier(r'C:/Users/Devotion/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# 识别眼睛
# eyeCascade = cv2.CascadeClassifier(r'C:/Users/Devotion/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml')

# 开启摄像头
# cap = cv2.VideoCapture(0)
# ok = True

result = []

# while ok:
img=cv2.imread("E:/idcard/000.jpg")
# 读取摄像头中的图像，ok为是否读取成功的判断参数
# ok, img = cap.read()
# 转换成灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸检测
# faces = faceCascade.detectMultiScale(
#     gray,     
#     scaleFactor=1.2,
#     minNeighbors=5,     
#     minSize=(32, 32)
# )

# 在检测人脸的基础上检测眼睛
# for (x, y, w, h) in faces:
#     fac_gray = gray[y: (y+h), x: (x+w)]
#     result = []
#     eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

#     # 眼睛坐标的换算，将相对位置换成绝对位置
#     for (ex, ey, ew, eh) in eyes:
#         result.append((x+ex, y+ey, ew, eh))

# 画矩形
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     print(x,y,x+w,y+h)
# for (ex, ey, ew, eh) in result:
#     cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
#     print(ex,ey,ex+ew,ey+eh)
# cv2.imshow('video', img)
img_std = cv2.resize(img, (748,460), interpolation=cv2.INTER_AREA) 

name_pic=cut_img(img_std,140,60,260,100)
nation_pic=cut_img(img_std,290,120,320,160)
sex_pic=cut_img(img_std,140,120,180,160)
# birth_y_pic=cut_img(img_std,140,170,220,220)
# birth_m_pic=cut_img(img_std,255,170,290,220)
# birth_d_pic=cut_img(img_std,320,170,360,220)
id_num_pic=cut_img(img_std,240,370,700,420)
address_pic=cut_img(img_std,140,230,460,310)
# time.sleep(1)

sex=ocr(sex_pic)
name=ocr(name_pic)
nation=ocr(nation_pic)
# birth=ocr(birth_y_pic)+'/'+ocr(birth_m_pic)+'/'+ocr(birth_d_pic)
id_num=ocr(id_num_pic)
address=ocr(address_pic)
# time.sleep(1)

id_info=name+','+sex+','+nation+','+id_num+','+address
print(id_info)

# 1. 创建文件对象
f = open('文件名.csv','a',encoding='utf-8')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
# csv_writer.writerow(["姓名","性别","民族","身份证号","地址"])

# 4. 写入csv文件内容
csv_writer.writerow([name,sex,nation,id_num,address])
# 5. 关闭文件
f.close()
cv2.waitKey(0)
# if k == 27:    #按 'ESC' to quit
cv2.destroyAllWindows()

# # 公民身份号码
# # cv2.rectangle(img_std, (60,370), (230,420), (255, 0, 0), 2)
# cv2.rectangle(img_std, (240,370), (700,420), (255, 0, 0), 2)
# # 姓名
# # cv2.rectangle(img_std, (60,50), (130,100), (255, 0, 0), 2)
# cv2.rectangle(img_std, (140,60), (260,100), (255, 0, 0), 2)
# # 性别
# # cv2.rectangle(img_std, (60,110), (130,160), (255, 0, 0), 2)
# cv2.rectangle(img_std, (140,120), (180,160), (255, 0, 0), 2)
# # 民族
# # cv2.rectangle(img_std, (220,110), (290,160), (255, 0, 0), 2)
# cv2.rectangle(img_std, (290,120), (320,160), (255, 0, 0), 2)
# # 出生
# # cv2.rectangle(img_std, (60,170), (130,220), (255, 0, 0), 2)
# # 年
# cv2.rectangle(img_std, (140,170), (220,220), (255, 0, 0), 2)
# # 月
# cv2.rectangle(img_std, (255,170), (290,220), (255, 0, 0), 2)
# # 日
# cv2.rectangle(img_std, (320,170), (360,220), (255, 0, 0), 2)
# # 住址
# # cv2.rectangle(img_std, (60,230), (130,280), (255, 0, 0), 2)
# cv2.rectangle(img_std, (140,230), (460,310), (255, 0, 0), 2)
# # cv2.imshow('video', img_std)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# # id_num_pic=img_std[370:420,240:700,:]
# cap.release()

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