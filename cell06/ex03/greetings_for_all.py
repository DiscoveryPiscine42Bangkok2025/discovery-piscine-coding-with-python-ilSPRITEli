def greetings(name="Noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
        return
    print(f"Hello, {name}.")


greetings("Alexandra")
greetings("Walt")
greetings()
greetings(42)


