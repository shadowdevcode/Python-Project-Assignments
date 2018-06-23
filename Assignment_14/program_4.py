# Write a Python program to combine each line from first file with the corresponding line in second file.

with open('test.txt') as fh1, open('output.txt') as fh2:    # Opening two files together in read mode by default.
    for line1, line2 in zip(fh1, fh2):   # line1 from test.txt, line2 from output.txt
        print(line1 + line2)
