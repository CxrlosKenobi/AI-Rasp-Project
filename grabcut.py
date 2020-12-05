# Image Segmentation
import numpy as np
import cv2

x = 'test'

while (x != 'end'):
    x = input('Image: ')
    if (x != 'end'):
        img = cv2.imread(x)
        mask = np.zeros(img.shape[:2], np.uint8)

        bgdModel = np.zeros((1,65), np.float64)
        fgdModel = np.zeros((1,65), np.float64)

        rect = (50, 50, 590, 400)
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
        img = img*mask2[:, :, np.newaxis]
        cv2.imwrite('masked-' + x, img)
