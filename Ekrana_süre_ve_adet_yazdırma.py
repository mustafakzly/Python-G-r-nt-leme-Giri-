import cv2
import numpy as np
import time
import os

start = time.time()
#başlangıç zamanını belirledik.

img = np.ones((650,650,3), np.uint8)
#Bir tane numpy modülüyle 1 lerden oluşan beyaz görüntü oluşturduk.

img[:,:] = (50,200,200)
#resime arka plan rengi verdik

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#haarcascade dosyasını tamıladık

image = cv2.imread("family3.jpg")
#yüz bulacağımız fotoğrafı okuduk

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Fotoğrafı gri formata dönüştürdük

faces = face_classifier.detectMultiScale(gray,1.2,7)
#fotoğraftaki yüzleri bulmak için faces diye tanımlama yaptık ve içine yüzleri aktardık.

font = cv2.FONT_HERSHEY_COMPLEX
dizi = []
#boş bir dizi oluşturdum

for (x,y,w,h) in faces:
    #for döngüsünde x,y,w,h kordinatlarını yüzde bulduk
    
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    #bulduğumuz kordinatlardaki yüzleri kare içerisine aldırdık 
    
    yuz = image[y:y+h,x:x+w]  
    dizi.append(yuz)
    #oluşturduğum diziye yuzleri ekledim
    
for i in range(0,len(faces)):
    os.chdir("C:/Users/Mustafa/Desktop/Python/OpenCV/yuz")
    #yeni yuz klasörü açtım ve orataya gittim
    
    cv2.imwrite(f"yuz{i}.jpg",dizi[i])
    #yuz klasörünün içine yüzleri yazdırdım
    
zaman = (time.time()- start)*1000
#ms cinsinden uygulamanın kaç ms çalıştığını buldum

if len(faces) >= 4:
    #Yüz sayısı 4 den büyükse 
    
    cv2.putText(img, f"{len(faces)} tane yuz bulundu.",(150,300),font,1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(img,f"Gecen sure : {zaman} ms",(10,350),font,1,(0,0,0),2,cv2.LINE_AA)
    #Ekrana süre ve kaç yüz olduğu yazdırılır.
    
else:
    cv2.putText(img,"Yuz bulunamadi",(190,320),font,1,(0,0,0),2,cv2.LINE_AA)
    #Yüz yoksa Yuz bulunamadı yazar  
    
cv2.imshow('image',img)
cv2.waitKey(0)