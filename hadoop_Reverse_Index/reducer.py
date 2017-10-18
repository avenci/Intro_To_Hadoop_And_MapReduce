#!/usr/bin/env python
import sys
import re

def reducer():
    curKey = None
    wordDict = {}
    totalHits = 0

    for line in sys.stdin:
        splitLine = line.split("\t")
        key = splitLine[0].strip()
        node = splitLine[1]

        if curKey and curKey != key:
            wordDict[curKey].append({"totalHits":totalHits})
            totalHits=0
        curKey = key

        totalHits += 1
        if key in wordDict:
            wordDict[key].append(node)
        else:
            wordDict[key] = [node]
    
    wordDict[curKey].append({"totalHits":totalHits})
    for word in wordDict:
        print "word: {0}, Nodes: {1}, {2}".format(word,set(wordDict[word][:-1]), wordDict[word][-1])

def main():
	reducer()

if __name__ == "__main__":
	main()
