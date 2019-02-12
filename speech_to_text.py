#!/usr/bin/env python
from os import environ, path
import pyaudio

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "/home/pi/jasper/pocketsphinx-5prealpha/model"
DATADIR = "/home/pi/jasper/pocketsphinx-5prealpha/test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', '/home/pi/jasper/4212.lm')
config.set_string('-dict', '/home/pi/jasper/4212.dic')
config.set_string('-keyphrase', 'forward')
config.set_float('-kws_threshold', 1e-50)


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024, exception_on_overflow=False)
    if buf:
         decoder.process_raw(buf, False, False)
    else:
         break
    if decoder.hyp() != None:
        print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print ("Detected keyword, restarting search")
        decoder.end_utt()
        decoder.start_utt()
