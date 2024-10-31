import cv2 as cv
# resmi oku
img = cv.imread("C:/Users/miruz/OneDrive/Belgeler/opencv/tech_ist/yesil_elma.jpg")
# img = cv.imread(r'data/yesil_elma.jpg')
#print(image)

# görüntün boyutlarını al(yükseklik, genişlik)
print(img.shape)
height,width =img.shape[:2]
channels = img.shape[2]
print(f"Yükseklik ve genişlik : {height}, {width}")
print(f"Kanal sayısı : {channels}")
print(f'Veri tipi : {img.dtype}')

# isteğe bağlı
cv.imshow("Elma",img)
cv.waitKey(0)
cv.destroyAllWindows