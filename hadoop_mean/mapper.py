#!/usr/bin/env python
import sys
import csv
import re
import string
from datetime import datetime
import calendar

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 6:
            print "{0}\t{1}".format(calendar.day_name[datetime.strptime(line[0], "%Y-%m-%d").weekday()],line[4])
def main():
    mapper()

if __name__ == "__main__":
    main()
