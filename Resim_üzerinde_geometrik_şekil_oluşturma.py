import cv2


img = cv2.imread("resim3.jpg")
#resmi okuduk
cv2.rectangle(img,(150,150),(400,400),(0,0,255),5)
#kare yaptık (x,x),(y,y),(renk seçimi),kalınlık
cv2.circle(img,(1228,1228),300,(150,150,150),5) 
#daire yaptık merkez , yarıçap , (renk seçimi),kalınlık
cv2.circle(img,(550,550),200,(190,190,190),-1)
#çember yaptık merkez , yarıçap , (renk seçimi),kalınlık = -1 olursa çember olur
cv2.ellipse(img,(256,256),(800,800),0,0,180,(255,100,0),10)
#elips merkez , uzunluk, yayın_açısı başlangıç ve bitiş , renk , kalınlık
cv2.namedWindow('çokgenler', cv2.WINDOW_NORMAL)
cv2.imshow('çokgenler',img)
#resmi gösterdik
cv2.waitKey(0)
#waitkey 0 yaparak resmi kapattırmadık
cv2.destroyAllWindows()
