import cv2

img = cv2.imread("resim2.jpg")
#öncelikle resmi okuyoruz.
rows , cols, _ = img.shape
#burada satır ve sütünların hangi uzunlukta olduklarını buluyoruz.
x = (rows/2)
y= (cols/2)
#Burada resmin tam orta noktasını bulmak için satır ve sütün sayılarını 2 ye bölüyoruz.
print("Resimin orta noktası = ",x,",",y)
#Resmin orta noktasını yazdırıyoruz.
