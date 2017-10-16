#!/usr/bin/env python
import sys
import re

def mapper():
    p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

    for line in sys.stdin:
        data = p.match(line)
        if not data:
            continue

        dataGroup = data.groups()
        if (len(dataGroup) == 7):
            ip, identity, uname, time, request, status, size  = dataGroup
            
            print "{0}".format(ip)
        
def main():
    mapper()

if __name__ == "__main__":
    main()
