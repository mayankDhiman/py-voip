import sys
import time

import socket
import pyaudio
import wave
from tkinter import *
import threading

# Audio Stream (PyAudio) Initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16 # Change to 8 if doesn't work
CHANNELS = 2
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

# Socket Initialization
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

# GUI Specifics
class VOIP_FRAME(Frame):    
    def OnMouseDown(self, event):
        self.mute = False
        self.speakStart()        
    def muteSpeak(self,event):
        self.mute = True
        print("You are now muted")
    def speakStart(self):
        t = threading.Thread(target=self.speak)
        t.start()                
    def speak(self):
        print("You are now speaking")
        while self.mute is False:
            data = stream.read(CHUNK)
            print(data)
            s.send(data)
            s.recv(size)
    def createWidgets(self):
        self.speakb = Button(self)
        self.speakb["text"] = "Speak"
        self.speakb.pack({"side": "left"})
        self.speakb.bind("<ButtonPress-1>", self.OnMouseDown)
        self.speakb.bind("<ButtonRelease-1>", self.muteSpeak)
    def __init__(self, master=None):
        self.mute = True
        Frame.__init__(self, master)
        self.mouse_pressed = False
        self.pack()
        self.createWidgets()

root = Tk()
app = VOIP_FRAME(master=root)
app.mainloop()
root.destroy()
s.close()
stream.close()
p.terminate()
