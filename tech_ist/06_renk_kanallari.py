import cv2 as cv
img = cv.imread(
    "C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/kizilsac3.jpg")
b, g, r = cv.split(img)

# mavi seç
img_mavi = cv.merge([r, g, b])

# fotoyu göster
cv.imshow("Mavi Sac", img_mavi)
cv.waitKey(0)
cv.destroyAllWindows()
