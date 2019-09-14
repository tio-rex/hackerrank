https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    cnt = 0
    for tag in root.iter():
        for attr in tag.attrib.items():
            cnt += 1
    return cnt
 
