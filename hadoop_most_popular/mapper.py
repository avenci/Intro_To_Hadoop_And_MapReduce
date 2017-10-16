#!/usr/bin/env python
import sys
import re

def mapper():
    p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

    regex_url = '(http:\/\/[^\/]+)?([^\?]*)(\?.*)?'
    request_url = re.compile(regex_url)

    for line in sys.stdin:
        data = p.match(line)
        if data:
            matches_url = request_url.match(data.groups()[4])
            if matches_url:
                url = matches_url.groups()[1]
                print "{0}".format(url.split(" ")[1])
        
def main():
    mapper()

if __name__ == "__main__":
    main()
