from gtts import gTTS
from playsound import playsound

audio = 'audio-gerado.mp3'
language = 'pt-br'

try:
    transform = gTTS(
        text = 'empate',
        lang = language
    )

    transform.save(audio)
    playsound(audio)
except:
    print('erro')