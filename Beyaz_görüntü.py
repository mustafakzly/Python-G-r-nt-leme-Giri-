import cv2
import numpy as np

beyaz = np.ones([300,300])
# üstteki satırda numpy kütüphanesinden 1 lerle bir matris oluşturduk 300x300 boyutlu(ones)
cv2.namedWindow("beyaz",cv2.WINDOW_NORMAL)
# namedWindow komutuyla getirdiğimiz resmin adını ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.imshow("beyaz",beyaz)
# ekranda göstereceğimiz değişkeni belirttik
cv2.waitKey(0)
# Açılan pencerenin kapanmaması için değer atadık(0 yazdığımızda klavyeden bir tuşa basana kadar çalışır)
cv2.destroyAllWindows("beyaz")
# Pencereyi kapatmak için kullanılır. İçine girilen isimi kapatır.

