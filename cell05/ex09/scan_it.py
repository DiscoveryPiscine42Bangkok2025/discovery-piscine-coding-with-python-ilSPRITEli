import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword, text = sys.argv[1], sys.argv[2]
    matches = re.findall(re.escape(keyword), text)
    print(len(matches))


