def famous_births(people: dict) -> None:
    # people: key -> dict(name, date_of_birth)
    sorted_entries = sorted(people.values(), key=lambda x: x["date_of_birth"])
    for entry in sorted_entries:
        print(f"{entry['name']} is a great scientist born in {entry['date_of_birth']}.")


women_scientists = {
 "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
 "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
 "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
 "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
 }
famous_births(women_scientists)