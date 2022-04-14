#Muhammad Fitrah Ramadhan
#F 551 20 081
#Kelas B
import cv2

img = cv2.imread("fitrah.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow("Citra Asli", img)
cv2.imshow("Citra GrayScale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()