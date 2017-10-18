#!/usr/bin/python
import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t')

A = None
B = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[1] == 'A':
        A = line[0]
        data_A = line[2:]

    elif line[1] == 'B':
        B = line[0]
        data_B = line[2:]

    if A == B:
        writer.writerow(data_B[:3] + [A] + data_B[3:] + data_A)
