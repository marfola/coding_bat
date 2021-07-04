#import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

''' Before starting the recorder, we declare the following variables. First is the sampling frequency and recording duration'''

#sampling frequency

freq = 44100

# recording duration

duration = 5

'''Now we start the recorder. This will create a Numpy array of the recorded audio'''

# Start the recorder with the given values of duration and sample frequencies

recording = sd.rec(int(duration*freq),samplerate=freq, channels=2)

# record audio for a given number of seconds

sd.wait()

''' Now that we're done recording the audio we can save it. First we use scipy'''
#this will convert the NumPy array into an audio file given sampling frequency

write("recording0.wav",freq, recording)

#next we use wavio file

wv.write("recording1.wav", recording, freq, sampwidth=2)

