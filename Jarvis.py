import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('Welcome Back Sir')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'idiyameen' in command:
                command = command.replace('idiyameen','')
            elif 'your name' in command:
                talk('I am idiyameen')
    except:
        print('Sorry')
        quit()
    return command

def run_baby():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('sure sir will play' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The Current time is ' + time + 'sir')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('what kind of question is this sir, I am not a living being')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif ('read' and 'pdf') in command:
        with sr.Microphone() as src:
            book = open('Tamil.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(pages)
            pagesstr = str(pages)
            talk('the pdf has a total of' + pagesstr + 'pages sir')
            talk('please tell the page number sir')
            pagen = listener.listen(src)
            compage = listener.recognize_google(pagen)
            pageno = int(compage)
            page = pdfReader.getPage(pageno)
            text = page.extractText()
            talk(text)
    elif 'stop' in command:
        print('Good Bye sir...')
        talk('Good Bye sir')
        quit()
    elif 'bye' in command:
        print('Good Bye sir...')
        talk('Good Bye sir')
        quit()
    elif 'whatsapp' in command:
        with sr.Microphone() as src:
            talk('please tell the phone number sir?')
            ph = listener.listen(src)
            comph = listener.recognize_google(ph)
            phnum = '+91' + comph
            print(phnum)
            talk('what is the message to be sent sir?')
            ms = listener.listen(src)
            comms = listener.recognize_google(ms)
            msg = comms
            print(msg)
            hour = datetime.datetime.now().strftime('%H')
            hr = int(hour)
            minute =datetime.datetime.now().strftime('%M')
            minu = int(minute) + 1
        pywhatkit.sendwhatmsg(phnum,msg,hr,minu)
    else:
        talk('Please say something sir')
while True:
    run_baby()

