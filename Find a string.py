https://www.hackerrank.com/challenges/find-a-string/problem
Find a string

def count_substring(string, sub_string):
    return (sum([1
                 for i in range(0, len(string) - len(sub_string) + 1)
                 if (string[i:(len(sub_string)+i)] == sub_string)]))
