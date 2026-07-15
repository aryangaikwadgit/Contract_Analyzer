import fitz

from src.ocr import OCR


class PDFParser:

    def __init__(self):

        self.ocr = OCR()

    def extract_text(self, pdf_path):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:

            page_text = page.get_text()

            text += page_text

        document.close()

        if len(text.strip()) > 50:

            return text

        print("Scanned PDF detected.")

        return self.ocr.extract_text(pdf_path)
