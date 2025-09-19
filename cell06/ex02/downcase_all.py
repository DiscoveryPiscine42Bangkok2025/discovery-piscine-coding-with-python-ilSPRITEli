import sys

class DowncaseIt:
    def downcase(self, text: str) -> str:
        return text.lower()

downcase = DowncaseIt().downcase
args = sys.argv[1:]

if not args:
    print("none")
else:
    for s in args:
        print(downcase(s))


