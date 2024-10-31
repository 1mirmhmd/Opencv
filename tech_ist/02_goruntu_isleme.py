import cv2 as cv
abs_path="C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/satranc3x3.jpg"

# imread() fonkdiyonu görseli okuyarak sayı dizisi şeklinde alır 
img = cv.imread(abs_path)
print(img)

# sayı dizisini tekrar görsel olarak gösterelim
cv.imshow("Satranc 3x3 @TechIst",img)

# belirli bir kısmı gösterme
print(img[300:400,:])

# bekle ve klavyeden bir sayı girildiğinde çık
cv.waitKey(0)
cv.destroyAllWindows()