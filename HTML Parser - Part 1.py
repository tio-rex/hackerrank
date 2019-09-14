https://www.hackerrank.com/challenges/html-parser-part-1/problem
HTML Parser - Part 1

from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_endtag(self, tag):
        print("End   : {}".format(tag))

    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

html = ""
for _ in range(int(input())):
    html += input()

parser = CustomHTMLParser()
parser.feed(html)
parser.close()
