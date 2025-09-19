class ArrayOfName:
    def array_of_names(self, people) -> list:
        full_names = []
        for first, last in people.items():
            full_names.append(f"{first.capitalize()} {last.capitalize()}")
        return full_names


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

array_of_names = ArrayOfName().array_of_names
print(array_of_names(persons))