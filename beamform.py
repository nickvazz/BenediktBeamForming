import math, os, platform, sys
import wave as wv
import tkinter as tk
import numpy as np
from tkinter import filedialog

def openFile():
   root = tk.Tk()
   if platform.system() != 'Darwin':  # This is just for convenience to make sure the file dialog is on top of other windows
       root.lift()
   else:
       os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
   root.withdraw()
   file_path = filedialog.askopenfilename() # If "cancel" was clicked in the dialog, we're ending the script with a message.
   if file_path == '':
       print('No file was selected. Restart the script to try again.')
       sys.exit()

   if file_path.rsplit('.', 1)[1] != 'WAV':
       print('Looks like the selected file was not an WAV file. Try again.')
       sys.exit()
   print('Opening source file ' + file_path + ' ...')
   return file_path

waveFile = openFile()

#print(os.path.dirname(waveFile))

r = wv.Wave_read(waveFile)

print(r.getnchannels())

print(r.readframes(1))

#w = wv.Wave_write('out.wav', channels=1)
#w.metadata.title = "Some Noise"
#w.metadata.artist = "The Artists"
#data = np.zeros((r.channels,512), np.float32, order='F')
#nframes = r.read(data)
#while nframes :
#  sys.stdout.write("."); sys.stdout.flush()
#  w.write(data[:,:nframes])
#  nframes = r.read(data)

if len(sys.argv) < 2: sys.exit(0)