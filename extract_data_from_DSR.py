import sys

from utils.extract_data_pdfminer import MyParser


class ParseDataFromDsr(object):
    if __name__ == '__main__':
        filePath = str(sys.argv[1])  # 'C:/Users/mmt6327/Desktop/Startup/DSR_Book Vol_1_2016_(English_Version)_Final.pdf'
        start_page_no = str(sys.argv[2])
        end_page_no = str(sys.argv[3])
        finalFilePath = str(sys.argv[4])
        print "Starting the process of getting the data from file %s (from page %s to page %s), and writing into file %s" % (filePath, start_page_no, end_page_no, finalFilePath)
        print '%s' % MyParser().process_pdf_pages(pdf=filePath, start_page_no=start_page_no, end_page_no=end_page_no, seperation_token="~")
