from ERSModule import *
import cv2
import numpy as np

def colormap(input,colors):
	height = input.shape[0]
	width  = input.shape[1]
	output = np.zeros([height,width,3],np.uint8)
	for y in range(0,height):
		for x in range(0,width):			
			id = int(input[y,x])
			for k in range(0,3):
				output[y,x,k] = colors[id,k]
	return output

nC = 100
img = cv2.imread("242078.jpg")
img_list = img.flatten().tolist()
h = img.shape [0]
w = img.shape [1]
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print grayImg.shape
label_list = ERS(img_list, h, w, nC)
label = np.reshape(np.asarray(label_list),(h,w)) ;

colors = np.uint8(np.random.rand(nC,3)*255)
output = colormap(label,colors)
cv2.imshow("img",img)
cv2.imshow("segmentation",output)
cv2.waitKey()
cv2.destroyAllWindows()
