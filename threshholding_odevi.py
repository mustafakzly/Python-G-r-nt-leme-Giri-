import cv2
import matplotlib as plt
img = cv2.imread("limon.jpg",0)
#resmi okuduk ve 2. parametreye yazdığımız 0 la grileştirdik
image = cv2.resize(img,(800,500))
#Resim büyük olduğu için resize ederek boyutunu ayarladım
blur = cv2.GaussianBlur(image, (5,5), 0)
#resmi gasu bluru ayarladım
ret,thresh = cv2.threshold(blur,210,255,cv2.THRESH_BINARY)
#resim 1 ve 0 lardan oluşturmak için threshold verdim
mask_inv = cv2.bitwise_not(thresh)
#resim arkası beyaz limonlar siyah olduğu için bitwise komutuyla 0 ve 1 lerin yerini değiştirdim
cv2.imshow("original",image)
cv2.imshow("thersh",mask_inv)
#resimleri gösterttim
cv2.waitKey(0)
#kapanmasın diye 0 verdim
cv2.destroyAllWindows()