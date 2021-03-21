# Spectral-music-tools
Scripts for spectral music composition.
The first script analyzes input wav-file, does FFT and shows its spectrum.
The main idea is to parse frequencies which amplitude is higher then the given one and to write them into the text-file.
The second script creates harmonic series by given fundamental frequency and randomly chooses values from it.
User can manage different parameters: number of overtones to generate, low and high border frequencies to output (because some overtones may be too high), number of values to generate. This way allows you to choose the range and you can group these frequencies to chords or use it like an instrument part.
