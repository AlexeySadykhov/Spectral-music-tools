import sys

c_line = list(map(float, input('Enter career line frequencies:').split()))
m_line = list(map(float, input('Enter modulator line frequencies:').split()))
g_line = list(map(int, input('Enter fm level line values:').split()))
if not len(c_line) == len(m_line) == len(g_line):
    print("Error. Lists' length must be the same.")
    sys.exit(1)


def create_spectrum(c, m, gain):
    array = [c]
    for i in range(1, gain+1):
        array.append(c + m * i)
        array.append(c - m * i)
    result = [x for x in array if 20 < x < 20000]
    result.sort()
    return result


def parse_to_lisp(lst):
    lst1 = ' '.join(str(item) for item in lst)
    lst2 = lst1.replace('[', '(')
    lst3 = lst2.replace(']', ')')
    lst4 = lst3.replace(',', '')
    return lst4


data = [create_spectrum(c_line[i], m_line[i], g_line[i]) for i in range(len(c_line))]
filename = input('Enter file name to save:')
file = open(f"{filename}.txt", "w")
file.write(parse_to_lisp(data))
file.close()
print('Done')
