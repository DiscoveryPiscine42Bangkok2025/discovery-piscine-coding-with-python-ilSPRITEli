import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for item in reversed(args):
        print(item)


