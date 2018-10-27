from StringIO import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser


class MyParser(object):

    def process_pdf_pages(self, pdf, start_page_no, end_page_no, seperation_token):

        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)

        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        codec = 'utf-8'

        device = TextConverter(rsrcmgr, retstr,
                               codec=codec,
                               laparams=laparams)

        interpreter = PDFPageInterpreter(rsrcmgr, device)

        pagenos = set(range(start_page_no - 1, end_page_no - 1))

        for page in PDFPage.get_pages(fp=file(pdf, 'rb'), pagenos=pagenos, password="", maxpages=0, caching=True):
            interpreter.process_page(page)

        self.records = []

        lines = retstr.getvalue().splitlines()
        for line in lines:
            self.handle_line(line)

        return ("%s" % seperation_token).join(self.records)

    def handle_line(self, line):
        self.records.append(line)
