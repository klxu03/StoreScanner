#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2

def decode(bc) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(bc)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data)

    return decodedObjects


# Main
if __name__ == '__main__':

    # Read image
    bc = cv2.imread('barcode.png')

    decodedObjects = decode(bc)
