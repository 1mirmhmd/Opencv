# farklı okuma modlari

import cv2 as cv
path="C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/satranc3x3.jpg"
img_color=  cv.imread(path,cv.IMREAD_COLOR)
# img_color=  cv.imread(path,1)

img_gray=  cv.imread(path,cv.IMREAD_GRAYSCALE)
# img_gray=  cv.imread(path,0)
# cv.imshow("Renkli",img_color)
# cv.imshow("Gri",img_gray)

path2="C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/yesil_elma.jpg"
img_color2=  cv.imread(path2,cv.IMREAD_COLOR)
# img_color2=  cv.imread(path2,1)

img_gray2=  cv.imread(path2,cv.IMREAD_GRAYSCALE)
# img_gray2=  cv.imread(path2,0)
cv.imshow("Renkli",img_color2)
cv.imshow("Gri",img_gray2)

cv.waitKey(0)
cv.destroyAllWindows()  
