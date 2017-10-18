#!/usr/bin/python
import sys
import csv

writer = csv.writer(sys.stdout, delimiter='\t')

A = None
B = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if data[1] == 'A':
        A = data[0]
        data_A = data[2:]

    elif data[1] == 'B':
        B = data[0]
        data_B = data[2:]

    if A == B:
        writer.writerow(data_B[:3] + [A] + data_B[3:] + data_A)
