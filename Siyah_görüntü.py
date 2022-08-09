import cv2
import numpy as np

siyah = np.zeros([300,300])
# üstteki satırda numpy kütüphanesinden 0 larla bir matris oluşturduk 300x300 boyutlu(zeros)
cv2.namedWindow("siyah",cv2.WINDOW_NORMAL)
# namedWindow komutuyla getirdiğimiz resmin adını ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.imshow("siyah",siyah)
# ekranda göstereceğimiz değişkeni belirttik
cv2.waitKey(0)
# Açılan pencerenin kapanmaması için değer atadık(0 yazdığımızda klavyeden bir tuşa basana kadar çalışır)
cv2.destroyAllWindows("siyah")
# Pencereyi kapatmak için kullanılır. İçine girilen isimi kapatır.
