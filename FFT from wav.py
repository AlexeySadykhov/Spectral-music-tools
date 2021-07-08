from math import log
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
from matplotlib import pyplot as plt

in_filename = input('Enter wav-file name to do FFT:')
s_rate, signal = wavfile.read(in_filename)
FFT = abs(fftpk.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
plt.plot(freqs[range(len(FFT)//2)],
         FFT[range(len(FFT)//2)])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()


def f_to_mc(f):
    d = 69 + 12 * log(f/440, 2)
    return int(d*100)


quant_step = int(input('Enter mc quantize step:'))
scale = [x for x in range(1548, 13508, quant_step)]


def nearest_value(lst, value):
    found = lst[0]
    for item in lst:
        if abs(item - value) < abs(found - value):
            found = item
    return found


low_amp = complex(input('Enter low amplitude border to parse:'))
result = set()

for x, y in zip(freqs[range(len(FFT)//2)],
                FFT[range(len(FFT)//2)]):
    if y >= low_amp:
        x = f_to_mc(x)
        x = nearest_value(scale, x)
        result.add(x)

out_file = open('spectrum_out.txt', 'w')
for item in result:
    out_file.write(str(item)+'\n')
out_file.close()

print('Ready')
