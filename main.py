from gtts import gTTS
import os

'''
pip install gtts
brew install mpg123
'''

if __name__ == '__main__':
    s = "Olá Serginho, como vão as raparigas?"
    file = "file.mp3"

    # initialize tts, create mp3 and play
    # tts = gTTS(s, lang='en', tld='com')
    tts = gTTS(s, lang='pt', tld='com.br')
    # tts = gTTS(s, lang='en', tld='co.uk')
    tts.save(file)
    os.system("mpg123 " + file)
