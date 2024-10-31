# farklı okuma modlari

import cv2 as cv
path="C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/satranc3x3.jpg"
img_color=  cv.imread(path,cv.IMREAD_COLOR)
# img_color=  cv.imread(path,1)

img_gray=  cv.imread(path,cv.IMREAD_GRAYSCALE)
# img_gray=  cv.imread(path,0)
cv.imshow("Renkli",img_color)
cv.imshow("Gri",img_gray)

cv.waitKey(0)
cv.destroyAllWindows          
