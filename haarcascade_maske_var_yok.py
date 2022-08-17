import cv2
import time

time = time.strftime('%H:%M:%S')
#Anlık zaman çektik ve %H:%M:%S sırayla saat dakika saniye verilerini aldık

mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")
#Haarcascade dosyasını ağız bulmak için tanımladık

cap = cv2.VideoCapture(0)
#Bilgisayarın kamerasını tanımladım

font = cv2.FONT_HERSHEY_COMPLEX
#Burada yazının fontunu ayarladık

while True:
    ret, img = cap.read()
    #kamerayı okuduk
    img = cv2.flip(img,2)
    #Kamera tersti düze çevirdik
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #yüz okumak için gri ekrana çevirdik
    
    mouths = mouth_cascade.detectMultiScale(gray,1.3,5)
    #Kameradaki yüz ifadesini bulduk
    
    cv2.putText(img,f"Time : {time}",(350,50),font,1,(255,0,0),2,cv2.LINE_AA)
    #kameranın sağ üstüne time modülünü ekledik 
    
    for(x,y,w,h) in mouths:
        #Ağızdaki x y w h kordinatlarını döngüye girdirdik
        
        kare = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        #Ağız bulursa kare içine almasını söyledik (0,255,255) sarı renkte bir kare
        
        roi_gray = gray[y:y+h , x:x+w]
        #gri resmin üzerinde herhangi istenen bir bölgeye pikseller ile erişip o bölge üzerinde istenen işlemlerin gerçekleştiridik.
        
        roi_color = img[y:y+h , x:x+w]
        #orjinal resmin üzerinde herhangi istenen bir bölgeye pikseller ile erişip o bölge üzerinde istenen işlemlerin gerçekleştiridik.
        
    if len(mouths) > 0:
        cv2.putText(img,"Maske yok",(450,450),font,1,(0,0,255),2,cv2.LINE_AA)
        #kameranın sağ altına maske yok yazdırdık yeşil renkte yüzünüzü tanımlarsa bu yazar.
    else: 
        cv2.putText(img,"Maske var",(50,450),font,1,(0,255,0),2,cv2.LINE_AA)
        #kameranın sol altına maske var yazdırdık kırmızı renkte yüzünüzü tanımlayamazsa bu yazar.
    
    cv2.imshow("img",img)
    #resmi gösterdik
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # burada esc basılınca çıkması komutunu verdik 
    
cap.release()
#VideoCapture sınıfını kapatır.

cv2.destroyAllWindows()