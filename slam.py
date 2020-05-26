#!/usr/bin/env python3
import cv2
import time
from display import Display

W = 1920//2
H = 1080//2

disp = Display(W, H)


class FeatureExtractor(object):
    GX = 16
    GY = 12
    def __init__(self):
        self.orb = cv2.ORB_create()

    def extract(self, img):
        # run detect in grid
        sy = img.shape[0]//self.GY
        sx= img.shape[1]//self.GX
        for ry in range(0, img.shape[0], sy):
            for rx in range(0, img.shape[1], sx):
                img_chunk = img[ry:ry+sy, rx:rx+sx]
                kp = self.orb.detect(img_chunk, None)
                for p in kp:
                    print(p)

fe = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img, (W, H))
    fe.extract(img)

    #for p in kp:
    #    u, v = map(lambda x: int(round(x)), p.pt)
    #    cv2.circle(img, (u,v), color=(0, 255,0), radius=3)
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture('test.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break


