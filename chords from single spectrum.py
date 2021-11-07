import random
from math import log


freq = float(input('Enter fundamental frequency:'))
num_of_ovtns = int(input('Enter number of overtones in spectrum:'))
low_border = float(input('Enter low border frequency:'))
high_border = float(input('Enter high border frequency:'))
num_of_chords = int(input('Enter number of chords to generate:'))
cnt_of_pitches_in_chord = int(input('Enter number of pitches in a chord:'))

main_spectrum = [freq*x for x in range(1, num_of_ovtns+1)]
array = []
i = 0
while i < num_of_chords:
    rand_index = random.randint(0, len(main_spectrum)-1)
    if rand_index == len(main_spectrum)-1 or rand_index + cnt_of_pitches_in_chord > len(main_spectrum)-1:
        array.append(main_spectrum[rand_index-cnt_of_pitches_in_chord:rand_index])
    else:
        array.append(main_spectrum[rand_index:rand_index+cnt_of_pitches_in_chord])
    i += 1


def f_to_mc(f):
    d = 69+12*log(f/440, 2)
    return int(d*100)


for x in array:
    for i, item in enumerate(x):
        if item < low_border:
            while item < low_border:
                item = item * 2
                if item >= low_border:
                    x.pop(i)
                    x.insert(i, f_to_mc(item))
        else:
            if item > high_border:
                while item > high_border:
                    item = item / 2
                    if item <= high_border:
                        x.pop(i)
                        x.insert(i, f_to_mc(item))
            else:
                x.pop(i)
                x.insert(i, f_to_mc(item))


def parse_to_lisp(x):
    x1 = ' '.join(str(n) for n in x)
    x2 = x1.replace('[', '(')
    x3 = x2.replace(']', ')')
    x4 = x3.replace(',', '')
    return x4


file_name = input('Enter file name to save the result:')
file = open(file_name + '.txt', 'w')
file.write(parse_to_lisp(array))
file.close()
print('Done')
