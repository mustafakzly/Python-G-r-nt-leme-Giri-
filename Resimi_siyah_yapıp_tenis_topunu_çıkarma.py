import cv2

img = cv2.imread("tenis.jpg")
#resmi okuduk
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#resmi convert yani ctvColor komutuyla griye döndürük
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
#ekranı ayarlayabilmek için window normal verdik
ret,mask = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
#resmi 1 ve 0 lardan oluşturduk.
cv2.imshow("resim",mask)
#resimi gösterttim
cv2.waitKey(0)
#kapanmasın diye 0 verdim
cv2.destroyAllWindows()