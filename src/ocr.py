import fitz
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCR:

    def extract_text(self, pdf_path):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:

            pix = page.get_pixmap(dpi=200)

            image = np.frombuffer(pix.samples, dtype=np.uint8)

            image = image.reshape(pix.height, pix.width, pix.n)

            page_text = pytesseract.image_to_string(image)

            text += page_text
            text += "\n"

        document.close()

        return text
