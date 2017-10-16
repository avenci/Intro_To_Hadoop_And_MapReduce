#!/usr/bin/env python
import sys
import re

def reducer():
	hits = 0
        curIP = None

	for line in sys.stdin:
            requestIP = line
            if not requestIP:
                continue

            if curIP and requestIP != curIP:
                print "{0}\t{1}".format(curIP,hits)
                hits = 0
            hits += 1
            curIP = requestIP



def main():
	reducer()

if __name__ == "__main__":
	main()
