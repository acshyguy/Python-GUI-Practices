##Pip install gTTS
from gtts import gTTS
import os

mytext = "Lagos is a beautiful city"
language = "en"

myobj = gTTS(text=mytext, lang= language,slow=False)

myobj.save("voice.mp3")

os.system("mediaplayer voice.mp3")