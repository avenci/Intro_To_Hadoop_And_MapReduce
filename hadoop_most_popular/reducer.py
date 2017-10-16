#!/usr/bin/env python
import sys
import re

def reducer():
	hits = 0
        highHits = 0
        highRequest = None
        curRequest = None

	for line in sys.stdin:
            requestRequest = line.strip()
            if not requestRequest:
                continue
            if ("/assets/css/combined.css" in requestRequest):
                hits += 1


        print "{0}\t{1}".format("/assets/css/combined.css", hits)

def main():
	reducer()

if __name__ == "__main__":
	main()
