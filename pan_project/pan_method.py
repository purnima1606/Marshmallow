from PIL import Image
import pytesseract
import re


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pancard_file = '.\Pancard.jpg'

def pancard(pancard_file):
  pancard_img = Image.open(pancard_file)
  # print(pancard_img)
  text = pytesseract.image_to_string(pancard_img)
  # print(text)
  if text:
    my_data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
    pan_data = {"Pancard no" :  my_data[0]}
    return pan_data
  else:
    pan_data = {"Pancard No": None}
    return pan_data
  # return pan_data

# print(pancard(pancard_file))

"""  
detail = pancard(pancard_file)
with open('details.txt','w')as file :
  file.append(detail)
  
"""




# def is_pancard(self, pancard_file):
 #    if pancard_file:
 #      pan_data = all_methods.pancard(pancard_file)
 #      # return pan_data
 #    else:
 #      pan_data = {"Pancard No": None}
 #      # return pan_data
 #    return pan_data



"""
FIR SX HIy
GOVT. OF INDIA

f
Strate TAA
INCOME TAX DEPARTMENT
Sart cea Wea Hrs
Permanent Account Number Card
KONPS9641A

PURNIMA SINGH

faat st al Father's Name

LAXMI NARAYAN SINGH
oe 27082018

wa eta,

DateofBirth ss # Wars

26/11/1997 A Feared Signature

{'Pancard no': 'KONPS9641A'}

"""
