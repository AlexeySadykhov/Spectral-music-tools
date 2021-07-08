from random import choice

try:
    freq = float(input('Enter fundamental frequency:'))
    num_of_ovtns = int(input('Enter number of overtones:'))
    low_border = float(input('Enter low border frequency:'))
    high_border = float(input('Enter high border frequency:'))
    num_of_freqs = int(input('Enter number of frequencies to generate:'))
except TypeError:
    print('Arguments must be rational')

data = []
for x in range(1, (num_of_ovtns+1)):
    data.append(freq*x)

file = open('spectrum.txt', 'w')
i = 0
while i < num_of_freqs:
    item = float(choice(data))
    if item < low_border:
        while item < low_border:
            item = item*2
            if item >= low_border:
                file.write(str(item)+'\n')
    else:
        if item > high_border:
            while item > high_border:
                item = item/2
                if item <= high_border:
                    file.write(str(item)+'\n')
        else:
            file.write(str(item)+'\n')
    i += 1
file.close()

print('Done')
