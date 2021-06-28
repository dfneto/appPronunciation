import os
from gtts import gTTS
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

'''
pip install gtts
brew install mpg123
'''

PATH = "./audios_compare/"
PATH_AUDIOS_GENERATED = "./audios_generated/"
PATH_FILE = "./transcripts/friends_6x23.txt"


def generate_audio_from(word, frequency):
    print(f"Generating audio for word {word} with {frequency} times in text")
    s = word
    file = f"{frequency}_{word}.mp3"

    # initialize tts, create mp3 and play
    tts = gTTS(s, lang='en', tld='com')
    # tts = gTTS(s, lang='pt', tld='com.br')
    # tts = gTTS(s, lang='en', tld='co.uk')
    tts.save(PATH_AUDIOS_GENERATED + file)
    print("Word generated!")
    # os.system("mpg123 " + file)


def convert_audio_to_wav(audio_name):
    os.system(f"ffmpeg -y -i {PATH}{audio_name}.mp3 -ac 1 {PATH}{audio_name}.wav")


def create_bow(text):
    tokens = [w for w in word_tokenize(text.lower())
              if w.isalpha()]
    stops = [t for t in tokens
             if t in stopwords.words('english')]
    no_stops = [t for t in tokens
                if t not in stopwords.words('english')]
    return Counter(no_stops), Counter(stops)


def read_file(file):
    with open(file) as f:
        text_file = f.read()
    return text_file


if __name__ == '__main__':
    transcript = read_file(PATH_FILE)
    words_of_bow, stops = create_bow(transcript)
    is_ready = input(f"We are ready to generate {len(words_of_bow)} words and we won't generate the "
                     f"{len(stops)} stop words. Are you sure? (y/n) ")
    if is_ready == "y":
        for word in words_of_bow:
            generate_audio_from(word, words_of_bow[word])
    else:
        pass
