https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
XML2 - Find the Maximum Depth

maxdepth = 0

def depth(elem, level):
    global maxdepth

    if level == maxdepth:
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)
 
