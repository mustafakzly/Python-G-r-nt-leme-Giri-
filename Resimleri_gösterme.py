import cv2
import os

for resim in os.listdir("C:/Users/Mustafa/Desktop/Python/OpenCV/"):
    if resim.endswith('.jpg'):
        img = cv2.imread(resim)
        cv2.namedWindow("goruntu",cv2.WINDOW_NORMAL)
        cv2.imshow("goruntu", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        