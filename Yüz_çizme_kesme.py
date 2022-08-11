import cv2

img = cv2.imread("girl.jpg")
#resimi okuduk
cv2.rectangle(img,(550,300),(1300,1400),(0,0,255),5)
#yüze gelecek şekilde bir kare oluşturduk (deneyerek)
kes = img[300:1400,550:1300]
#yüze denk getirdiğimiz kareyi kestik
cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)
# namedWindow komutuyla imshowla aynı adı ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.namedWindow("goruntu2",cv2.WINDOW_NORMAL)
# namedWindow komutuyla imshowla aynı adı ve büyüyüp küçültülebilen bir hal verdik(window_normal)
cv2.imshow("goruntu2", kes)
#kesilen resimi gösterdik
cv2.imshow("goruntu", img)
#normal resimi gösterdik
cv2.imwrite("kesilenyuz.jpg",kes)

cv2.waitKey(0)
#kapanmaması için 0 yazdık
cv2.destroyAllWindows()
#çıkış yapmak için yazdık