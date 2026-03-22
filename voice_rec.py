import sounddevice as sd
import wavio as wv


frequency = 44100
duration = 5

recording=sd.rec(int(frequency*duration),samplerate=frequency,channels=2)
sd.wait()

wv.write('record.wav',recording,frequency,sampwidth=2)