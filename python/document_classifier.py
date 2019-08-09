#!/usr/bin/python3 -u
import os
import time
import subprocess
import PyPDF2
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

print('Running as: ' + os.environ['USER'])

DOWNLOADS_DIR = '/home/huy/Downloads/'
DOCUMENTS_DIR = '/home/huy/Documents/'

class FileHandler(PatternMatchingEventHandler):
    patterns = ['*.pdf', '*.epub']
    @staticmethod
    def __move(path, category):
        filename = path.split('/')[-1]
        os.rename(path, DOCUMENTS_DIR + category + '/' + filename)
        # subprocess.call(['su', os.environ['LOGNAME'], '-c', 'notify-send ' + '"Document Classifier" ' +'"New downloaded file has been sent to [' + category + ']"'])
        subprocess.call(['notify-send', 'Document Classifier',  filename + ' has been sent to [' + category + ']'])

    def process(self, event):
        with open(event.src_path, 'rb') as pdf:
            pdfReader = PyPDF2.PdfFileReader(pdf)
            if (pdfReader.getNumPages() <= 20):
                FileHandler.__move(event.src_path, 'articles')
            else:
                FileHandler.__move(event.src_path, 'ebooks')

    def on_created(self, event):
        self.process(event)

# class Classifier:
#     def __init__(self, path):
#         self.__pdf = open(path, 'rb')
#         self.__pdfReader = PyPDF2.PdfFileReader(self.__pdf)
#     def predict_category(self):
#         self.__pdfReader.

if __name__ == '__main__':
    observer = Observer()
    observer.schedule(FileHandler(), path=DOWNLOADS_DIR)
    observer.start()
    print("Documents Classifier is running")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
