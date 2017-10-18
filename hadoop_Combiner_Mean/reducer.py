#!/usr/bin/env python
import sys
import re

def reducer():
    curKey = None
    totalHits = 0
    totalValue = 0

    for line in sys.stdin:
        splitLine = line.split("\t")
        day = splitLine[0]
        value = splitLine[1]

        if curKey and curKey != day:
            print "{0}\t{1}".format(day, totalValue/totalHits)
            totalHits=0
            totalValue=0
        curKey = day 

        totalHits += 1
        totalValue += float(value)

    print "{0}\t{1}".format(curKey, totalValue/totalHits)
def main():
	reducer()

if __name__ == "__main__":
	main()
