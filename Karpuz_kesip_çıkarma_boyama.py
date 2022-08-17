import cv2


img = cv2.imread("karpuz.jpg")
#resmi okuduk
cv2.imshow("resim",img)
cv2.waitKey(0)
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#Resmin rengini gri yaptık

edged = cv2.Canny(gray,10,40)
#canny bulma algoritması ile kenarlarını bulduk

contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#konturledik
       
for i in contours:
    
    x,y,w,h = cv2.boundingRect(i)
    #Kontur çerçeve noktalarını hesaplayıp cv2.rectangle() metoduyla etraflarına dikdörtgen çizdik
    
    if w>200 and h>100:
        #belli bir alan tanımladık
        break
kes = img[y:y+h, x:x+w]
#kesilecek köşegenleri belirttik

cv2.imwrite("kesik_karpuz.jpg",kes)
#kesilen parçayı dosyaya kaydettik

cv2.drawContours(img, contours, -1,(0,0,255),3) 
#Çıkan konturleri çizdirdik. 



cv2.imshow("kesilen_karpuz",kes)
#kesilen parçayı ekranda gösterttik

cv2.waitKey(0)