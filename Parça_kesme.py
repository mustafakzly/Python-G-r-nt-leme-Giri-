import cv2

img = cv2.imread("resim2.jpg")
# resmi okuyoruz.
kesilen_resim = img[400:800, 500:1250]
#kesceğimiz yerin x ve y kordinatlarını giriyoruz
cv2.imshow("kesilen resim",kesilen_resim)
#kesilen resimi göstermek için imshow kullanıyoruz
cv2.imshow("resim",img)
#orjinal resimi göstermek için imshow kullanıyoruz
cv2.waitKey(0)