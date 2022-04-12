from gtts import gTTS
from PyPDF2 import PdfFileReader
import os

# The text that you want to convert to audio
book = open("The Python Book_ The ultimate guide to coding with Python ( PDFDrive ).pdf", "rb")
book_read = PdfFileReader(book)
book_pages = book_read.getNumPages()

book_string = ""

for n in range(book_pages):
    first_page = book_read.getPage(n)
    book_string += first_page.extractText()


my_text = book_string

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the
# converted audio should have a high speed.

my_obj = gTTS(text=my_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file

my_obj.save("book.mp3")

# Playing the converted file
os.system("start welcome.mp3")
