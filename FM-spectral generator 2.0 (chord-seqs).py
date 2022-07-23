c_line_s = input('Enter career line freqs:').split()
c_line_l = []
for i, item in enumerate(c_line_s):
    c_line_s[i] = float(item)
    c_line_l.append(c_line_s[i])

m_line_s = input('Enter modulator line freqs:').split()
m_line_l = []
for i, item in enumerate(m_line_s):
    m_line_s[i] = float(item)
    m_line_l.append(m_line_s[i])

q_line_s = input('Enter fm level line values:').split()
q_line_l = []
for i, item in enumerate(q_line_s):
    q_line_s[i] = float(item)
    q_line_l.append(q_line_s[i])


def create_spectrum(c, m, qtty):
    array = []
    array.append(c)
    i = 1
    while i <= qtty:
        array.append(c+m*i)
        i += 1

    i = 1
    while i <= qtty:
        array.append(c-m*i)
        i += 1

    result = [x for x in array if x > 20]
    result.sort()
    return result

array = []
for i in range(len(c_line_l)):
    array.append(create_spectrum(c_line_l[i], m_line_l[i], q_line_l[i]))


def parse_to_lisp(x):
    x1 = ' '.join(str(n) for n in x)
    x2 = x1.replace('[', '(')
    x3 = x2.replace(']', ')')
    x4 = x3.replace(',', '')
    return x4

file = open('my_fm_spectral_chords.txt', 'w')
file.write(parse_to_lisp(array))
file.close()
print('Done')
