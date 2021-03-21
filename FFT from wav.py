import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
from matplotlib import pyplot as plt

in_filename = input('Enter wav-file name to do FFT:')
s_rate, signal = wavfile.read(in_filename)
FFT = abs(fftpk.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))
plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

low_amp = complex(input('Enter low amplitude border to parse:'))
out_file = open('spectrum_out.txt', 'w')
for x, y in zip(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)]):
    if y >= low_amp:
        out_file.write(str(x)+'\n')
out_file.close()

print('Ready')
