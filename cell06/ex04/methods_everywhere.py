import sys


def shrink(text: str) -> str:
    return text[:8]


def enlarge(text: str) -> str:
    padding = max(0, 8 - len(text))
    return text + ("Z" * padding)


args = sys.argv[1:]
if not args:
    print("none")
else:
    for item in args:
        if len(item) > 8:
            print(shrink(item))
        elif len(item) < 8:
            print(enlarge(item))
        else:
            print(item)


