# kırmızı rengi yeşile çevirme
import cv2 as cv
img = cv.imread("C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/elma.jpg")
cv.imshow("Kırmızı Elma", img)
b, g, r = cv.split(img)

# kirmizi ve yeşil kanalları değiştir
img_yesil = cv.merge([b, r, g])
# yeşil renkli elmayı göster
cv.imshow("Yeşil Elma", img_yesil)

img_mavi = cv.merge([r, g, b])
cv.imshow("Mavi Elma", img_mavi)

cv.waitKey(0)
cv.destroyAllWindows
