import cv2
img = cv2.imread("AS.JPEG")
grayimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("original", img)
cv2.imshow("grayimg", grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
