import pyttsx3
from PyPDF2 import PdfFileReader

def get_pdf_file():
    pdf_file = input("Enter name of pdf file: ")
    if not pdf_file.endswith('.pdf'):
        pdf_file = pdf_file + '.pdf'
    return pdf_file

def get_text(pdf_file):
    reader = PdfFileReader(open(pdf_file, 'rb'))

    for page in range(reader.numPages):
        text = reader.getPage(page).extractText()
        clean_text = text.strip().replace('\n', ' ')
        return clean_text

def get_audio_name():
    audio_name = input("Enter name of audio file: ")
    return audio_name + '.mp3'

def make_audio(text):
    audio_name = get_audio_name()
    speaker = pyttsx3.init()
    speaker.save_to_file(text, audio_name)
    speaker.runAndWait()
    speaker.stop()


if __name__ == '__main__':
    text = get_pdf_file()
    make_audio(text)

