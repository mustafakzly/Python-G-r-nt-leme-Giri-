import cv2
import os

input_size = 227
# 3 farklı değerde ffotoğrafımız var ondan birini gireceğiz. 128,227,416

back_img = cv2.imread(f"vida{input_size}.jpeg")
#bu gireceğimiz resmi okuduk.

klasor = os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/vida")
#vidalarımızın olduğu klasörü klasor diye değişkenin içine atadık.

os.mkdir(f"{input_size}_{input_size}")
#Verdiğimiz boyutlarda dosya oluşturduk.

for i in klasor:
   #klasörün değeri kadar i yi döndürdük
   
    if i.endswith('.jpg'):
        #klasördeki sonu jpg ile bitenleri seçtirdik.
        
       vida_img = cv2.imread(f"{i}")
       #vidaları i değeri olarak okuduk.
       
       cols,rows,_ = vida_img.shape
       #vidaların satır, sütun sayılarını buldurduk
       
       deger = back_img.copy()
       #Başta okuttuğumuz back_img dosyasını üst üste vidaları eklemesin diye bir degere atadık
       
       x = int((input_size - cols)/2)
       y = int((input_size - rows)/2)
       #Vidaları resmin ortasına koyacagımız için satır ve sütunların hangi kolondan başlayacağını yazdırdık.
       
       deger[x:x + cols,y:y + rows] = vida_img
       #vidaları back_imgın orta noktasına gelecek şekilde yapıştırdık.
       
       cv2.imwrite(f"{input_size}_{input_size}/{i}",deger)
       #oluşturduğumuz dosyanın içine bu vidaları atadık.
       
       if input_size == 416:
           #Eğer back_img boyutu 416 ya eşit olursa
           
           gray= cv2.cvtColor(deger, cv2.COLOR_BGR2GRAY)
           #bütün çıktıları gri formata dönüştürdük
           
           cv2.imwrite(f"{input_size}_{input_size}/{i}",gray)
           #Bu dönüştürdüğümüz gri resimleri ilgili olan dosyaya atadık.