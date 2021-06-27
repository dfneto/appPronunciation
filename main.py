from gtts import gTTS
import os


'''
pip install gtts
brew install mpg123
'''

PATH = "./audios_compare/"


def generate_audio_from(text):
    s = text
    file = f"{text}_gtts.mp3"

    # initialize tts, create mp3 and play
    tts = gTTS(s, lang='en', tld='com')
    # tts = gTTS(s, lang='pt', tld='com.br')
    # tts = gTTS(s, lang='en', tld='co.uk')
    tts.save(file)
    os.system("mpg123 " + file)


def convert_audio_to_wav(audio_name):
    os.system(f"ffmpeg -y -i {PATH}{audio_name}.mp3 -ac 1 {PATH}{audio_name}.wav")


if __name__ == '__main__':
    pass


