import cv2


resim = cv2.imread("resim1.jpg")
# Öncelikle bir resmi okuduk imread komutu ile
resim = cv2.resize(resim, (300, 300))
# resize komutu ile önce değişkeni sonra kaça kaç pixel olacağını belirttim
cv2.imshow("resim", resim)
# ekranda göstereceğimiz değişkeni belirttik  
cv2.waitKey(0)
# Açılan pencerenin kapanmaması için değer atadık(0 yazdığımızda klavyeden bir tuşa basana kadar çalışır)
cv2.destroyAllWindows("resim")
# Pencereyi kapatmak için kullanılır. İçine girilen isimi kapatır.