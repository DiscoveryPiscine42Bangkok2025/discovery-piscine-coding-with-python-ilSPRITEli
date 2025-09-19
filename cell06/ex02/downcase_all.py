import sys

class DowncaseIt:
    def downcase(self, text: str) -> str:
        return text.lower()

obj = DowncaseIt()
args = sys.argv[1:]

if not args:
    print("none")
else:
    for s in args:
        print(obj.downcase(s))


