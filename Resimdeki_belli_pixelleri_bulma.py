import cv2

img = cv2.imread("resim1.jpg",0)
#görselimizi okuyoruz
rows , cols = img.shape
#satır ve sütün ka. adet olduğunu hesaplatıyoruz
toplam = 0
#toplam kaç adet olduğunu bulmak için bir 0 değerli toplam oluşturuyoruz.
for a in range(0,cols-1):
    #a dan yani 0 dan sütunun bir eksik değerine kadar döndürüyoruz
    for b in range(0,rows-1): 
        #b dan yani 0 dan satırın bir eksik değerine kadar döndürüyoruz
       if img[b][a] == 50:
           #önce sütunu yazdığımız için b artacak a sabit kalacak içdeki döngü sürekli döneceği için img[b][a] yazarak elemanı buluyoruz
           print(b," - ",a)
           #hangi sütün ve satırda olduğunu yazıyor
           toplam += 1
           #50 sayısını buldukça toplamı 1 arttırıyoruz
print(toplam)
#toplamı yazdırıyoruz
