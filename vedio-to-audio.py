import moviepy.editor
from tkinter.filedialog import *

vid = askopenfilename()

vedio=moviepy.editor.VideoFileClip(vid)

aud=vedio.audio
aud.write_audiofile("demo.mp3")

print("--end--")