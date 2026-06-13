from pypdf import PdfReader


class PDFParser:

    def __init__(self, pdf_path):

        self.pdf_path = pdf_path

    def extract_text(self):

        reader = PdfReader(self.pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text

        return text