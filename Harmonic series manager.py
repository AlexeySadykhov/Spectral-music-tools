import random


freq = float(input('Enter fundamental frequency:'))
num_of_ovtns = int(input('Enter number of overtones in spectrum:'))
low_border = float(input('Enter low border frequency:'))
high_border = float(input('Enter high border frequency:'))
num_of_freqs = int(input('Enter number of frequencies to generate:'))


def random_variation(s, l, h, q):
    data = []
    for i in range(q):
        item = random.choice(s)
        if item < l:
            while item < l:
                item = item*2
                if item >= l:
                    data.append(item)
        else:
            if item > h:
                while item > h:
                    item = item/2
                    if item <= h:
                        data.append(item)
            else:
                data.append(item)
    return data


def write_to_file(data, file_name):
    file = open(file_name + '.txt', 'w')
    for item in data:
        file.write(str(item) + '\n')
    file.close()


spectrum = [freq * i for i in range(1, num_of_ovtns+1)]
array = random_variation(spectrum, low_border, high_border, num_of_freqs)
filename = input('Enter file name to save:')
write_to_file(array, filename)
print('Done')
