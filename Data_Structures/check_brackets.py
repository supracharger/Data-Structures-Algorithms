# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    inverse = {'(':')', '[':']', '{':'}'}
    for i, nxt in enumerate(text):
        if nxt in "([{":
            # Process opening bracket
            opening_brackets_stack.append((nxt, i))

        elif nxt in ")]}":
            # Process closing bracket
            if len(opening_brackets_stack)==0 or nxt!=inverse[opening_brackets_stack[-1][0]]:
                return i + 1
            del opening_brackets_stack[-1]
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[-1][1] + 1
    return 'Success'


def main():
    text = input()

    #text = '{}[]'
    #text = '[()]'
    #text = '(())'
    #text = '{[]}()'
    #text = '{'
    #text = '{[}'
    #text = 'foo(bar)'
    #text = 'foo(bar[i)'
    #text = '}'
    #text = '[](()'

    print(find_mismatch(text))


if __name__ == "__main__":
    main()
