from PIL import Image
from pytesseract import pytesseract

# Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image
path_to_image = 'Images/sampletext1.png'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

# Extract text from image
text = pytesseract.image_to_string(img)

print(text[len(text) - 2])

import SAP_HANA_connection as con

sap_con = con.sap_hana_connect();
con_update = sap_con.conn.cursor()
sql_update = f"UPDATE KIRAN_SCHEME.SAMPLE_TABLE SET VALUE = VALUE + {text[len(text) - 2]}"
con_update.execute(sql_update)
con_update.close()


