# Spectral-music-tools
Scripts for spectral music composition.

"FFT wav parser" script analyzes input wav-file, does FFT and shows its spectrum.
The main idea is to parse frequencies which amplitude is higher then the given one, convert them to midicents and to write into the text-file.

"Harmonic series manager" script creates harmonic series by given fundamental frequency and randomly chooses values from it.
User can manage different parameters: number of overtones to generate, low and high border frequencies to output (because some overtones may be too high), number of values to generate. This way allows you to choose the range and you can group these frequencies to chords or use it like an instrument part.

"Random chords from single spectrum" is similar to "Harmonic series manager", but it automatically creates chords from these random spectral partials.

"FM-spectral generator" is the most powerful one. Using this script you can transform into music score the whole process of frequency modulation synthesis. The task of the script is to create a spectral chord sequence. It can be achieved if we will use just three lists: list of career frequencies, list of modulator frequencies and a list of a gain. User can just type theese values to console and he will easily get a result in a text file.
