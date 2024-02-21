# Voice-Assistant-Jarvis-
I present you a Basic Voice Assistant developed using Python inspired from Iron Man. I have named mine as "Idiyameen". He is capable of playing a song, send a WhatsApp message, reply to u if u want to have a date, read a file aloud for you, tell you the time, welcome you, tell you a joke, quit when you ask him to stop or say bye, etc.

To Change voice to Female go to line 11 of the code and place this --->  engine.setProperty('voice',voices[1].id)

To Change Assistant's Name [replace 'idiyameen' from line 23 to line 26]:
            if 'idiyameen' in command:
                command = command.replace('idiyameen','')
            elif 'your name' in command:
                talk('I am idiyameen')
                
VOICE COMMANDS:

If you instruct "play 'song name'" he plays the song via youtube.

If your instruction has the keyword 'date' he would reply his opinion about dating you.

If your instruction has the keyword 'time' he would tell the time.

If your instruction has the keyword 'who is' he would give a short description about the person you ask about. For example, "who is Dr. A.P.J.Abdul Kalam".

If you ask "are u single" he would reply.

If your instruction has the keyword 'joke' he would tell you a joke.

If your instruction has the keywords 'read' and 'pdf' he would read the pdf u have linked.
     book = open('Tamil.pdf', 'rb') --> Replace 'Tamil.pdf' with the pdf file u want him to read in line 56.

If your instruction has the keyword 'WhatsApp' he would help you send a message to any mobile phone number via WhatsApp.
     phnum = '+91' + comph --> Repalce '+91' with your Country's Dialing Code in line 82.

If your instruction has the keyword 'stop' or 'bye' he would stop execution and quit. 
     

