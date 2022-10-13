from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# 영어 문장
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# tts_en = gTTS(text = text, lang = 'en')
# tts_en.save(file_name)
# playsound(file_name)

# 한글 문장
# text = '윤길아 자니? 일어나 학교가야지 맘마먹자'
# tts_ko = gTTS(text = text, lang = 'ko')
# tts_ko.save(file_name)
# playsound(file_name)    # mp3파일 재생



# 긴 문장(파일에서 불러와서 처리) 
with open('sample.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

tts_ko = gTTS(text = text, lang = 'ko')
tts_ko.save(file_name)
playsound(file_name)