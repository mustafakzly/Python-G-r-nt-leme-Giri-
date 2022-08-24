import cv2
import random

face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
#Yüzü bulmak için haarcascade xml dosyasını çağırdık.

img = cv2.imread("girl.jpg")
#Yüzü bulacağımız resmi okuttuk

img = cv2.resize(img,(600,800))
#Resmin yeniden boyutlandırdık.

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Resmi gri formata çevirdik.

face = face_detect.detectMultiScale(gray_img, 1.3,3)
 
for (x, y, w, h) in face:
    #Yüzü bulmak için yükseklik genişlik x ve y kordinatlarını tanımladık
    
    yuz = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0),2)  
    #Yüzü kare içine aldırdık
    
for i in range(y,y+h):
    for j in range(x,x+w):
        #çift for ile kare olarak çizdirdiğimiz yüzü döndürdük
        
        sayi = random.randint(0,255)
        #random sayi atadık
        
        yuz[i][j] = sayi
        #bütün piksellerine ulaşıp bu piksellere random renkler atadık
        
        cv2.imshow("yuz", yuz) 
        #Yüzü gösterdik
        
    if cv2.waitKey(1000) & 0xff == 27:
        break
    #esc ile çıkmak için komut yazdık
        
        
 
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()  # herhangi bir tuşa basınca kapatmak için