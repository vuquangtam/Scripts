try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
img_path = "picture.png"
print(pytesseract.image_to_string(Image.open(img_path), lang='eng'))
print("Done")
