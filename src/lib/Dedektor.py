import cv2
import numpy as np
from src.lib.Resim import Resim
import os


class Dedektor:
    # def __init__(self,image1,image2):
    #     self.image1 = image1
    #     self.image2 = image2
    @staticmethod
    def olcekle(image1, image2):
        if(image1.resimBoyutunuGetir() > image2.resimBoyutunuGetir()):
            print("Image1 Büyük")
            image1.yenidenBoyutlandir(image2.width, image2.height)
        else:
            print("Image2 Büyük")
            image2.yenidenBoyutlandir(image1.width, image1.height)

    @staticmethod
    def fark(image1, image2):
        # Birinci resme göre fark alma.
        fark = cv2.subtract(image1.image, image2.image)

        # ikinci resme göre fark alma.
        fark2 = cv2.subtract(image2.image, image1.image)

        Conv_hsv_Gray = cv2.cvtColor(fark, cv2.COLOR_BGR2GRAY)
        Conv_hsv_Gray2 = cv2.cvtColor(fark2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(
            Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        ret, mask2 = cv2.threshold(
            Conv_hsv_Gray2, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # Resimlere kırmızı maske uygulama.
        fark[mask != 255] = [0, 0, 255]
        fark2[mask2 != 255] = [0, 0, 255]
        #image1.image[mask] = np.concatenate(image1.image[mask], [0, 0, 255])
        # bu satırı blend etmek için yazdım.

        # iki resmin farkının tek bir değişkende depolandığı yer burası.
        fark = cv2.addWeighted(fark, 1.0, fark2, 1.0, 1.0)
        image1.image[mask != 255] = [0, 0, 255]
        image2.image[mask != 255] = [0, 0, 255]

        # bütün karşılaştırma bunun üzerinde yapılacak.
        son = cv2.addWeighted(image1.image, 0.5, image2.image, 0.5, 1.0)

        fark = cv2.addWeighted(son, 0.5, fark, 1.0, 1.0)

        """
        -> Amacım iki resimin orjinal hâlini alıp karıştırarak bütün farkları/içerikleri tek 
        bir resimde toplmak.

        -> İki defa fark alma amacım ise matematiksel olarak x-y ile y-x in sonuçlarının x=y değilse
        farklı olacağı için iki durumlu da farkını alıp bunları tek bir resimde birleştiriyorum. Böylece
        bütün bulunmuş farkları tek bir resimde toplayarak bulunan farkları yeni bir resim üretmek için toplamış oluyorum.

        -> Sonra elimdeki iki resmin karıştırılmış(blend) hâli ile bütün farklarının tek bir resim üzerinde
        toplanmış hâlini karıştırarak tek bir resim elde ediyorum. Böylece iki katman üst üste geldiğinden
        resimlerde boyanmış olan kırmızı alanlar iki resim arasındaki fark oluyor.
        
        """

        p = os.getcwd()
        p = p.replace("\\", "/")
        cv2.imwrite(p + "/test_images/sonuc.png", fark)
        return Resim(p + "/test_images/sonuc.png")
