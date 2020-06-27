from PIL import Image
import pytesseract
im=Image.open(r"C:\Users\Anirudh\Desktop\sp.png")
text=pytesseract.image_to_string(im,lang="eng")
print(text)
