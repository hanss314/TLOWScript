import sys
from response import tlow as interpreter

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as code:
        interpreter(code.read())

