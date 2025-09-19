class Greetings:
    def greet(self, name="noble stranger"):
        if not isinstance(name, str):
            print("Error! It was not a name.")
            return
        print(f"Hello, {name}.")

greetings = Greetings()

greetings.greet("Alexandra")
greetings.greet("Walt")
greetings.greet()
greetings.greet(42)


