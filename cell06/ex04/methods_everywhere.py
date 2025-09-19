import sys

class ShrinkEnlarge:
    def shrink(self, text: str) -> str:
        return text[:8]

    def enlarge(self, text: str) -> str:
        padding = max(0, 8 - len(text))
        return text + ("Z" * padding)

shrink = ShrinkEnlarge().shrink
enlarge = ShrinkEnlarge().enlarge

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


