import numpy as np
import cv2
import sys

face_cascade = cv2.CascadeClassifier('frontalface_default.xml')
print(face_cascade.empty())
specs_ori = cv2.imread('koz.png', -1)

cap = cv2.VideoCapture(0) #webcame video
cap.set(cv2.CAP_PROP_FPS, 30)

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
    print(faces)
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:

            ymin = int(y)
            ymax = int(y + h)
            # print(ymin, ymax)

            roi_color = img[ymin:ymax, x:x+w]

            specs = cv2.resize(specs_ori, (w, h), interpolation=cv2.INTER_CUBIC)
            transparentOverlay(face_glass_roi_color,specs)

    cv2.imshow('Face', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cv2.imwrite('img.jpg', img)
        break

cap.release()

cv2.destroyAllWindows()