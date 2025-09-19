class FindTheRedheads:
    def find_the_redheads(self, family: dict) -> list:
        return [name for name, color in family.items() if color == "red"]


dupont_family = {
 "florian": "red",
 "marie": "blond",
 "virginie": "brunette",
 "david": "red",
 "franck": "red"
 }

find_the_redheads = FindTheRedheads().find_the_redheads
print(find_the_redheads(dupont_family))