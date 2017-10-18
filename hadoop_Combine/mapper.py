#!/usr/bin/env python
import sys
import csv
import re
import string
from datetime import datetime
import calendar

def mapper():
    writer = csv.writer(sys.stdout,delimiter='\t')
    reader = csv.reader(sys.stdin, delimiter='\t')
    reader.next()
    for line in reader:
        if len(line) == 5:
            writer.writerow([line[0]] + ["A"] + line[1:])
        elif len(line) == 19:
            writer.writerow([line[3]] + ["B"] + line [:3] + line[5:10])
def main():
    mapper()

if __name__ == "__main__":
    main()
