import pyttsx3 as p
import PyPDF2

#open book
book = open('example.pdf', 'rb') #inseret PDF as the first parameter. Second parameter is to read
pDFReader = PyPDF2.PdfFileReader(book)
pages = pDFReader.numPages
print(pages)


speaker = p.init()
for num in range(15, pages): #first parameter is starting page
    page = pDFReader.getPage(num)
    text = page.extractText()
    newVoiceRate = 140
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[3].id)   
    speaker.setProperty('rate',newVoiceRate)
    speaker.say(text)
    speaker.runAndWait()
