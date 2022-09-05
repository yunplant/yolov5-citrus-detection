import cv2

label = open('# .txt PATH')
img = cv2.imread('# img PATH',cv2.IMREAD_COLOR)
lines = label.readlines()
i = 0

for line in lines :
    read = line.split(" ")
    x1 = int(read[1])
    y1 = int(read[2])
    x2 = int(read[3])
    y2 = int(read[4])
    cropped_img = img[y1:y2, x1:x2]
    i += 1
    cv2.imshow(str(i), cropped_img)

cv2.imshow('original', img)
cv2.waitKey(0)