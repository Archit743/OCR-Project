import re
from pdfminer.high_level import extract_pages, extract_text

#parses every element in the pdf be it text , images or anyhing else in the page

for page_layout in extract_pages("C:\My Codes\PythonCodes\Aekiusoft Proposal.pdf"):
    for element in page_layout:
        print(element)

#parses all the text
text = extract_text("C:\My Codes\PythonCodes\Aekiusoft Proposal.pdf")
print(text) 

#finding patterns in the text
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}") #this asks to find elemnt starting with uppercase or lowercase followed by 1 comma and 1 space
matches = pattern.findall(text)
print(matches)
#to extract words which followed the pattern
words = [n[:-2] for n in matches]
print("here are the matched words:-  ",words)


#extracting images from the pdf
import fitz   #from PyMuPDF
import PIL.Image   #from pillow
import io
pdf = fitz.open("C:\My Codes\PythonCodes\Aekiusoft Proposal.pdf")
counter = 1 #a counter to keep track of the number of images
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]#extension of the image
        img.save(open(f"image{counter}.{extension}","wb"))
        counter += 1

#extracting tables from the pdf
import tabula
tables = tabula.read_pdf("C:\My Codes\PythonCodes\Aekiusoft Proposal.pdf",pages = "all")
print(tables)