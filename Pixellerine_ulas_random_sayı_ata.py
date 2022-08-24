import random
import cv2

img = cv2.imread("apple.jpg",0)
#resmi okuduk

rows,cols = img.shape
#resmin satır ve sütun sayılarını bulduk

for i in range(0,rows):
    
    for j in range(0,cols):
        #Çift for ile önce satırları sonra sütunları döndürdük
        
        sayi = random.randint(0,255)
        #sayi diye değişkene random sayılar atadık
        
        img[i][j] = sayi
        #Resimdeki piksellere ulaşıp bu piksellere random sayılarla değiştirdik
        
        cv2.imshow("resim",img)
        #Resmi gösterdik
        
    if cv2.waitKey(1000) & 0xff == 27:
        break
    #Resimden esc basınca durmasını istedik.
    
cv2.destroyAllWindows()