import sys

if len(sys.argv) != 2:
    print("none")
else:
    try:
        answer = input("What was the parameter? ")
    except EOFError:
        answer = ""

    if answer == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")


