import os
os.chdir("/Users/matthewphillips/Downloads")

f = open('rosalind_ini5.txt', 'r')
lines = f.readlines()
line_count = len(lines)

h = open('output.txt', 'w')

for i in range(line_count):
    if i % 2 == 1:
        h.write(lines[i])

h.close()