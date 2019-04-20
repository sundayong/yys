
import cv2


image = cv2.imread("JT3.jpg")
#image2 = image[597: 417, 485:494, :]
image2 = image[414: 504, 591:689]
#invite_meanValue = np.mean(srcImg[407: 504, 884:992, :] - invite)
cv2.imwrite("invite1.png", image2)
#cv2.imshow("image-1", image2)
#cv2.waitKey(0)

