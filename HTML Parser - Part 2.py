https://www.hackerrank.com/challenges/html-parser-part-2/problem
HTML Parser - Part 2

from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        type = "Multi-line" if "\n" in data else "Single-line"
        print(">>> {} Comment".format(type))
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input().rstrip() + "\n"

parser = CustomHTMLParser()
parser.feed(html)
parser.close()
