try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

def pic2text(pic_path):
    return pytesseract.image_to_string(Image.open(img_path), lang='eng')

if __name__ == "__main__":
    pic2text("picture.png")
