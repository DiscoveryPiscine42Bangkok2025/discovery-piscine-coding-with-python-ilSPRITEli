class AddOne:
    def add_one(self, value: int) -> int:
        return value + 1


number = 5
print(number)
add_one = AddOne().add_one
number = add_one(number)

print(number)


