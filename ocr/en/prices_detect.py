from PIL import Image
import pytesseract
import argparse
import cv2
import os, re

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to input image to be OCR\'d')
ap.add_argument('-p','--preprocess', type=str, default='thresh', help='type of preprocessing to be done')
args = vars(ap.parse_args())

print(f'image is {args["image"]}')

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args['preprocess'] == 'thresh':
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args['preprocess'] == 'blur':
    gray = cv2.medianBlur(gray, 3)

filename = f'{os.getpid()}.png'
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow('Image', image)
cv2.imshow('Output', gray)
cv2.waitKey(0)