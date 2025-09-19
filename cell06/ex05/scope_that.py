class AddOne:
    def add_one(self, value: int) -> int:
        return value + 1


number = 5
print(number)
obj = AddOne()
number = obj.add_one(number)

print(number)


