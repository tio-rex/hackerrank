https://www.hackerrank.com/challenges/merge-the-tools/problem
Merge the Tools!

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        output = ''
        unique_letters = set()
        for letter in string[i:i + k]:
            if letter not in unique_letters:
                output += letter
                unique_letters.add(letter)
            else:
                pass
        print(output)
        
