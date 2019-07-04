# String = input()
# Width = int(input())
# St=list(String[i:i+Width] for i in range(0,len(String),Width))
# [print(tr) for tr in St]

import textwrap

def wrap(string, max_width):
    #St=list(string[i:i+max_width] for i in range(0,len(string),max_width))
    return "\n".join(string[i:i+max_width] for i in range(0,len(string),max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)