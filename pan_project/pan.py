from PIL import Image
import pytesseract
import re


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pancard_file = '.\Pancard.jpg'

# def pancard(pancard_file):
#   pancard_img = Image.open(pancard_file)
#   # print(pancard_img)
#   text = pytesseract.image_to_string(pancard_img)
#   # print(text)
#   if text:
#     my_data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
#     pan_data = {"Pancard no" :  my_data[0]}
#     return pan_data
#   else:
#     pan_data = {"Pancard No": None}
#     return pan_data

# print(pancard(pancard_file))

"""
{'Pancard no': 'KONPS9641A'}
"""
# *******************************************************************************************************************************

def pancard(pancard_file):
  pancard_img = Image.open(pancard_file)
  # print(pancard_img)
  text = pytesseract.image_to_string(pancard_img)
  print(text)
  if text:
    """ 
    my_data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
    pan_data = {"Pancard no" :  my_data[0]}
    return pan_data
    """
    my_data = re.findall("\d{2}/\d{2}/\d{4}" , text)
    dob = {"dob" : my_data[0]}
    return dob

  else:
    pan_data = {"Pancard No": None}
    return pan_data


print(pancard(pancard_file))


"""
{'dob': '26/11/1997'}

"""
# ************************************************************************************************************************************************

def pancard(pancard_file):
  pancard_img = Image.open(pancard_file)
  # print(pancard_img)
  text = pytesseract.image_to_string(pancard_img)
  print(text)
  if text:
    """ 
    my_data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
    pan_data = {"Pancard no" :  my_data[0]}
    return pan_data
    """
    """ 
    my_data = re.findall("[A-Z]+", text)
    name = {"name": my_data[0]}
    return name
    """
    count = 0
    for line in text:
      if line.strip() == re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text):
        num = count +1
      else:
        count += 1
  else:
    pan_data = {"Pancard No": None}
    return pan_data


print(pancard(pancard_file))
