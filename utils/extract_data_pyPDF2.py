import PyPDF2

pdfFileObj = open('C:/Users/mmt6327/Desktop/Startup/DSR_Book Vol_1_2016_(English_Version)_Final.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print("Number of pages in the files:- %s\n" % str(pdfReader.numPages))

pageObj = pdfReader.getPage(13)

print(pageObj.extractText())

pdfFileObj.close()
