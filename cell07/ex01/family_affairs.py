def find_the_redheads(family: dict) -> list:
    return [name for name, color in family.items() if color == "red"]


dupont_family = {
 "florian": "red",
 "marie": "blond",
 "virginie": "brunette",
 "david": "red",
 "franck": "red"
 }
print(find_the_redheads(dupont_family))