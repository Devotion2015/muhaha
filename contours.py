import cv2
import numpy as np
import matplotlib.pyplot as plt


def Extract(op_image, sh_image):
	binary, contours,_ = cv2.findContours(op_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours.remove(contours[0])
	max_x, max_y, max_w, max_h = cv2.boundingRect(contours[0])
	color = (0, 255, 0)
	for c in contours:
		x, y, w, h = cv2.boundingRect(c)
		cv2.rectangle(op_image, (x, y), (x + w, y + h), color, 1)
		cv2.rectangle(sh_image, (x, y), (x + w, y + h), color, 1)
		if max_w < w:
			max_x = x
			max_y = y
			max_w = w
			max_h = h
			cut_img = sh_image[max_y:max_y+max_h, max_x:max_x+max_w]
	# cv2.imshow("The recognized enlarged image", op_image)
	# cv2.waitKey(0)
			cv2.imshow("The recognized binary image", sh_image)
			cv2.waitKey(0)
	return cut_img

if __name__ == '__main__':
    # 一共三张做测试用身份证图像
    path = 'E:/001.jpg'
    #path = 'IDcard02.png'
    #path = 'IDcard.jpg'
    id_card = cv2.imread(path)
    # cv2.imshow('Original image', id_card)
    # cv2.waitKey(0)
    # 将图像转化成标准大小
    id_card = cv2.resize(id_card, (1200, 820))
    # cv2.imshow('Enlarged original image', id_card)
    # cv2.waitKey(0)
    # 图像二值化
    imgray=cv2.cvtColor(id_card,cv2.COLOR_BGR2GRAY)
    ret, binary_img = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('Binary image', binary_img)
    # cv2.waitKey(0)

    # RECTANGULAR
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # RECTANGULAR
    kernel2 = cv2.getStructuringElement(cv2.MORPH_DILATE, (5, 5))
    #close_img = cv.morphologyEx(binary_img, cv.MORPH_CLOSE, kernel)
    # The corrosion treatment connects the ID Numbers
    erode = cv2.erode(binary_img, kernel, iterations=10)
    # cv2.imshow('Eroded image', erode)
    # cv2.waitKey(0)

    cut_img = Extract(erode, binary_img.copy())
    cv2.imshow("cut_img", cut_img)
    cv2.waitKey(0)
