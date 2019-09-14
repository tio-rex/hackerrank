https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html = '\n'.join([input() for _ in range(int(input()))])
parser = CustomHTMLParser()
parser.feed(html)
parser.close()
