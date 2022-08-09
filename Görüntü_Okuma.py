import cv2

goruntu = cv2.imread("goruntu.jpg")
# Öncelikle bir resmi okuduk imread komutu ile
cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)
# namedWindow komutuyla getirdiğimiz resmin adını ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.imshow("goruntu",goruntu)
# ekranda göstereceğimiz değişkeni belirttik
cv2.waitKey(0)
# Açılan pencerenin kapanmaması için değer atadık(0 yazdığımızda klavyeden bir tuşa basana kadar çalışır)
cv2.destroyAllWindows("goruntu")
# Pencereyi kapatmak için kullanılır. İçine girilen isimi kapatır.

