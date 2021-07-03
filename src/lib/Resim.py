import cv2
import numpy


class Resim:
    def __init__(self, image):
        self.src = image
        img = cv2.imread(image)
        self.image = img
        w, h, c = img.shape
        self.height = w
        self.width = h
        #self.channels = c

    def resimBoyutunuGetir(self):
        return self.width * self.height

    def siyahBeyaz():
        return ""

    def goster(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def yenidenBoyutlandir(self, genislik, yukseklik):
        self.image = cv2.resize(
            self.image, (genislik, yukseklik), interpolation=cv2.INTER_AREA)
        w, h, c = self.image.shape
        self.width = w
        self.height = h
