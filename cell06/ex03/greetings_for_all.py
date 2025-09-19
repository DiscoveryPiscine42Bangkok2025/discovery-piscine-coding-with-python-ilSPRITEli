class Greetings:
    def greet(self, name="noble stranger"):
        if not isinstance(name, str):
            print("Error! It was not a name.")
            return
        print(f"Hello, {name}.")

greetings = Greetings().greet

greetings("Alexandra")
greetings("Walt")
greetings()
greetings(42)


