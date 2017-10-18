#!/usr/bin/env python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) == 19:
            body = line[4]
            node_id = line[0]
            body = re.sub('[^a-zA-Z0-9 \n\.]', ' ', body)
            words = body.strip().split()
            for word in words:
                print "{0}\t{1}".format(word.lower(),node_id)
def main():
    mapper()

if __name__ == "__main__":
    main()
