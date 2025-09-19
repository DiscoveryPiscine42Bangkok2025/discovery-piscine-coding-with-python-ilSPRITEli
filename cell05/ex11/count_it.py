import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for value in args:
        print(f"{value}: {len(value)}")


