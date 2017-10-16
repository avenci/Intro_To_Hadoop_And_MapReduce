#!/usr/bin/env python
import sys

def reducer():
	saleCount = 0
        saleTotal = 0

	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 1:
			continue
                saleTotal += float(data[0])
                saleCount += 1



        print "saleTotal: {0}, saleCount: {1}".format(saleTotal, saleCount)

def main():
	reducer()

if __name__ == "__main__":
	main()
