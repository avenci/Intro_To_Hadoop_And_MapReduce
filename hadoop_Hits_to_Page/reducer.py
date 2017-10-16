#!/usr/bin/env python
import sys
import re

def reducer():
	hits = 0
        curPath = None

	for line in sys.stdin:
            requestPath = line.split(" ")[1]
            if not requestPath:
                continue

            if curPath and requestPath != curPath:
                print "{0}\t{1}".format(curPath,hits)
                hits = 0
            hits += 1
            curPath = requestPath



def main():
	reducer()

if __name__ == "__main__":
	main()
