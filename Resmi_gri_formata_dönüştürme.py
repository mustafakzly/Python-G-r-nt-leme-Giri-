import cv2

goruntu = cv2.imread("goruntu.jpg")
# Öncelikle bir resmi okuduk imread komutu ile
resim_gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
# Rengi convert ederek gri formata dönüştürür
cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)
# namedWindow komutuyla getirdiğimiz resmin adını ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.imshow("goruntu",resim_gri)
# ekranda göstereceğimiz değişkeni belirttik
cv2.waitKey(0)
# Açılan pencerenin kapanmaması için değer atadık(0 yazdığımızda klavyeden bir tuşa basana kadar çalışır)
cv2.destroyAllWindows("goruntu")
# Pencereyi kapatmak için kullanılır. İçine girilen isimi kapatır.

