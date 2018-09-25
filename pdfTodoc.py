import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

import win32com
import win32com.client
def readPDF(srcpath,topath):
    f = open(srcpath,'rb')
    parse = PDFParser(f)
    pdfdoc = PDFDocument()
    parse.set_document(pdfdoc)
    pdfdoc.set_parser(parse)
    pdfdoc.initialize()

    if not pdfdoc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        manager = PDFResourceManager()
        laParam = LAParams()
        device = PDFPageAggregator(manager,laparams=laParam)
        interpreter = PDFPageInterpreter(manager,device)
        word = win32com.client.Dispatch('Word.Application')
        word.Visible = True
        docx = word.Documents.Add()

        r = docx.Range(0,0)
        for page in pdfdoc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x,LTTextBoxHorizontal):
                    str = x.get_text()

                    r.InsertAfter(str)

        docx.SaveAs(topath)
        docx.Close()
        word.Quit()
