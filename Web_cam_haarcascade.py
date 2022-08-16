import cv2
import time

time = time.strftime('%H:%M:%S')
#Anlık zaman çektik ve %H:%M:%S sırayla saat dakika saniye verilerini aldık
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Haarcascade dosyasını yüz bulmak için tanımladık
cap = cv2.VideoCapture(0)
#Bilgisayarın kamerasını tanımladım
font = cv2.FONT_HERSHEY_COMPLEX
#Burada yazının fontunu ayarladık
while True:
    ret, img = cap.read()
    #kamerayı okuduk
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #yüz okumak için gri ekrana çevirdik
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    #Kameradaki yüz ifadesini bulduk
    cv2.putText(img,f"Time : {time}",(350,50),font,1,(255,0,0),2,cv2.LINE_AA)
    #kameranın sağ üstüne time modülünü ekledik 
    for(x,y,w,h) in faces:
        #Yüzdeki x y w h kordinatlarını döngüye girdirdik
        kare = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        #Yüz bulursa kare içine almasını söyledik (0,255,255) sarı renkte bir kare
        roi_gray = gray[y:y+h , x:x+w]
        #gri resmin üzerinde herhangi istenen bir bölgeye pikseller ile erişip o bölge üzerinde istenen işlemlerin gerçekleştiridik.
        roi_color = img[y:y+h , x:x+w]
        #orjinal resmin üzerinde herhangi istenen bir bölgeye pikseller ile erişip o bölge üzerinde istenen işlemlerin gerçekleştiridik.
    if len(faces) > 0:
        cv2.putText(img,"Yuz var",(450,450),font,1,(0,255,0),2,cv2.LINE_AA)
        #kameranın sağ altına yazı var yazdırdık yeşil renkte
    else: 
        cv2.putText(img,"Yuz yok",(50,450),font,1,(0,0,255),2,cv2.LINE_AA)
        #kameranın sol altına yazı yok yazdırdık kırmızı renkte
    
    cv2.imshow("img",img)
    #resmi gösterdik
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # burada esc basılınca çıkması komutunu verdik 
cap.release()
#VideoCapture sınıfını kapatır.
cv2.destroyAllWindows()