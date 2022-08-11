import cv2

img = cv2.imread("kaplumbaga.jpg")
#Resmi okuduk
cols,rows,_ = img.shape
#Satır ve sütun sayılarını bulduk.
print(cols)
print(rows)
deg = 30
#döngüye girmeden kaçar derece artacaksa onu belirledik
for i in range(0,13):
#döngü oluşturduk biz 1 tam tur atmasını istediğimiz için 360/30 = 12 kere çalıştırdık
     R = cv2.getRotationMatrix2D((cols/10,rows/10),deg*i,0.4)
     #Döndürmek için bu komutu kullanıyoruz sadece her döngüde dönmesi için deg*i yapmamız gerekiyor
     Rotated_resim = cv2.warpAffine(img,R,(cols,rows))
     cv2.imshow("resim2", Rotated_resim)
     #resmi gösteriyoruz
     cv2.waitKey(1000)
     #1 saniyede bir değişmesini istiyoruz
     cv2.destroyAllWindows()
