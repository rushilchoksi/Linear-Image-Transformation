from PIL import Image
import numpy as np
from tkinter import filedialog

originalImage = Image.open(filedialog.askopenfilename())
widthOriginal, heightOriginal = originalImage.size
if widthOriginal >= 250 and heightOriginal >= 250:
    if widthOriginal == heightOriginal:
        originalImage.show()
        pixelMap = originalImage.load()
        widthOriginal, heightOriginal = originalImage.size
        for i in range(widthOriginal):
            for j in range(i+1, heightOriginal):
                pixelMap[i, j], pixelMap[j, i] = pixelMap[j, i], pixelMap[i, j]

        originalImage.save("Transpose#1.jpg")
        pixelMapTranspose = np.asarray(originalImage)
        transposedImage = Image.open("Transpose#1.jpg")
        pixelMapNew = transposedImage.load()
        widthTranspose, heightTranspose = transposedImage.size
        for i in range(widthTranspose):
            for j in range(i+1, heightTranspose):
                pixelMapNew[j, i], pixelMapNew[i, j] = pixelMapNew[i, j], pixelMapNew[j, i]

        reverseTranspose = pixelMapTranspose[::-1]
        newImage = Image.fromarray(reverseTranspose)
        newImage.save("ReverseTransposed.jpg")
        finalImage = Image.open("ReverseTransposed.jpg")
        pixelMapFinal = finalImage.load()
        widthFinal, heightFinal = finalImage.size
        for j in range(int(heightFinal)):
            for i in range(j+1, int(widthFinal)):
                pixelMapFinal[i, j], pixelMapFinal[j, i] = pixelMapFinal[j, i], pixelMapFinal[i, j]

        finalImage.show()
        finalImage.save("Final.jpg")
    else:
        print("Please choose a square image")
else:
    print("Please choose an image having dimensions above 250*250")
