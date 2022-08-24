import shutil
import os

os.chdir('C:/Users/Mustafa/Desktop/Python/OpenCV/Deneme1')
dst_dir = ("C:/Users/Mustafa/Desktop/Python/OpenCV/Deneme2")
dosya_isimleri = os.listdir('C:/Users/Mustafa/Desktop/Python/OpenCV/Deneme1')
dizi = dosya_isimleri

for f in os.listdir():
    shutil.copy(f, dst_dir)
    
for sayac , resim in enumerate(dizi, start = 1):
    print(sayac, dizi)

  