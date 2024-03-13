from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
import cv2
'''
# Input and Output Locations
pdf_path = 'sample_Image.pdf'
output_folder = r'/Users/nishuchoudhary/Desktop/'

# routine to extract individual images from the complete file
images = convert_from_path('/Users/nishuchoudhary/PycharmProjects/STRIDE_ML/Exploration/KA_CrashReports_2.pdf')
number_of_images = len(images)

# Iterate through image list
for index, image in enumerate(images):
    #Check for every second page - odd page number
    if index == 3:
        print(type(image))
        cropped_region = (50, 50, 150, 150)
        text = pytesseract.image_to_string(image)


cropped_region = (50, 50, 150, 150)
image = images[3]
cropped_image = image.crop(cropped_region)
cropped_image.show()  # To display the cropped image
cropped_image.save("cropped_example.jpg")
'''

# Sample image to get the sub-routine
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pixel Coordinates (x,y): {x}, {y}")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

image = cv2.imread('output_image.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_click)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

