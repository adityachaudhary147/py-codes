# python3

from collections import namedtuple
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w')
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0:
                return i+1
            if are_matching(opening_brackets_stack[-1],next):
                opening_brackets_stack.pop()
                continue
            else:
                return i+1
            pass
    if len(opening_brackets_stack)!=0:
        return i+1


    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

    # Printing answer, write your code here
if __name__ == "__main__":
    main()
