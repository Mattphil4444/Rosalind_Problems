
# changing my working directory to downloads
import os
os.chdir("/Users/matthewphillips/Downloads")

# opening the file
f = open('rosalind_ini6 (1).txt', 'r')
# reading in the contents of the file as one long string
text = f.read()
# stripping out the new line markers
text = text.replace('\n',' ')

# splitting the file contents into a list of words
words = text.split()

# making an empty dictionary to write to
counts = {}

# this for loop creates a key for any words not in the dictionary
# and adds one to its value every time it shows up in the file
for i in words:
    if not i in counts:
        counts[i] = 0
    counts[i] += 1

# making an output file to write to
outfile = open('output.txt', 'w')

# this loop writes each key and it's corresponding value into the output
# file on a new line
# .items returns a view object that displays a list of
# a dictionary's (key, value) tuple pairs
for key, value in counts.items():
    outfile.write(key + ' ' + str(value) + '\n')

