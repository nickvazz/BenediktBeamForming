import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

import glob

import soundfile as sf
from scipy.io import wavfile
from scipy import signal

from bokeh.io import curdoc
from bokeh.layouts import layout, column, row, widgetbox
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure, output_file, show, reset_output
from bokeh.models.widgets import Select

reset_output()

# output_file('dashboard2.html')

# move to utilities
def convert_wav(filename):
    data, samplerate = sf.read(filename)
    converted_filename = filename.split('.')[0] + '-32bit.wav'
    sf.write(converted_filename, data, samplerate, subtype='PCM_32')

# for f in files:
#     convert_wav(f)
files = glob.glob('audio_files/*.wav')

def data_list(val, lst):
    return [x for x in lst if x != val]


def update_file(attrname, old, new):
    data_select.options = data_list(new, files)
    
    update()
    
def update(selected=None):
    filename = data_select.value

    make_total_spectrogram(filename)
    
    layout = row(widgetbox(data_select), p)

    show(layout)
    
    
    
def make_total_spectrogram(filename):
    rate, data = wavfile.read(filename)

    # need to make it sum all 4 channels
    f, t, Sxx = signal.spectrogram(data[:,0],rate)
    Sxx = np.log(Sxx)
    plt.pcolormesh(t,f,Sxx)
    plt.savefig('tmp/spectrogram_top.png')
    
    p = figure(x_range=(0,max(t)), y_range=(0,max(f)), 
               active_drag=None, plot_width=800, plot_height=200)
    p.image(image=[Sxx], x=0, y=0, dw=max(t),dh=max(f), palette='Spectral11')

    return p
    

def mic_spectrogram(filename):
    rate, data = wavfile.read(filename)

    plots = []
    for i in range(4):
        # need to make it sum all 4 channels
        f, t, Sxx = signal.spectrogram(data[:,i],rate)
        Sxx = np.log(Sxx)
        plt.pcolormesh(t,f,Sxx)
        plt.savefig('tmp/spectrogram_top.png')

        p = figure(x_range=(0,max(t)), y_range=(0,max(f)), 
                   active_drag=None, plot_width=800, plot_height=200)
        p.image(image=[Sxx], x=0, y=0, dw=max(t),dh=max(f), palette='Spectral11')
        
        plots.append(p)

    return column(p)

print files


data_select = Select(title='File:', value=files[0], options=data_list(files[0], files))
data_select.on_change('value', update_file)

p = make_total_spectrogram(files[0])

col = mic_spectrogram(files[0])


layout = column(row(widgetbox(data_select), p), col)

show(layout)

