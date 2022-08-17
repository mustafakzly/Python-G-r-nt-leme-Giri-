import os
import cv2
import shutil

klasor = os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/images")
#Klasörün içindeki dosyaları klasör adlı değişkene atadım.

arrays = []
arrays2 = []
#Boş bir dizi oluşturdum.

os.chdir("C:/Users/Mustafa/Desktop/Python/OpenCV/images")
#Dosya konumunu images dosyası olarak belirledim
for i in range(0,len(klasor)):
    #klasörün içindeki eleman sayısı kadar for ile döndürdüm
    
    img2 = cv2.imread(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}")
    #Dosyanın içindeki bütün fotoğrafları okudum
    
    cols,rows,_ = img2.shape
    #Bu resimlerin satır , sütun değerlerini buldum
    
    deger = str(rows)
    #Bu değerleri string'e çevirip deger diye degişkenimin içine atadım
    
    arrays.append(deger)
    #Boş dizime deger'de dönen değerleri ekledim
    
    if arrays[i] == '1920' or arrays[i] == '2400' or arrays[i] == '640': 
        #Dizi[i] sırayla dosyanın degerlerine baktırdım 1920 , 2400 , 640 degerlerini bulsun diye
        
        ad = f"{deger}_images" 
        #Bir ad değişkeni atadım içine 1920, 2400, 640 degerlerinde dosya oluşturabilmek için
        
        if os.path.isdir(f"{deger}_images"):
            #Dosyanın var olup olmadığını kontrol ettim.
            
            shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}",ad)
            #Burada eğer dosya varsa ad değişkenindeki dosyaya o boyuttaki dosyaları ekledim.
            
        else:    
            #Dosya yoksa
        
            yeni_dosya = os.mkdir(ad)
            #Yeni dosya oluşturup 1920, 2400, 640 degerleri adında dosyaları oluşturdum.
            
            shutil.move(f"C:/Users/Mustafa/Desktop/Python/OpenCV/images/{klasor[i]}",ad)
            #Dönen satır sayılarına göre o addaki dosyaya aynı satırlı ifadeleri eklettim.
    