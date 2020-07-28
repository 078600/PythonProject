from pyzbar import pyzbar
import cv2
from tkinter import *
import os

def read(photo_name):
    image=cv2.imread(photo_name)
    
    barcodes=pyzbar.decode(image)
    for barcode in barcodes:
        barcodeData=barcode.data.decode("utf-8")
        return(barcodeData)
        cv2.waitKey(0)
    root.mainloop()
