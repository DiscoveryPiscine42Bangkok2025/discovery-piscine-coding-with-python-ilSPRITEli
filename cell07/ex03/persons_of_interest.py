class FamousBirth:

    def get_birth_date(self, person_dict: dict) -> str:
        return person_dict["date_of_birth"]

    def famous_births(self, people: dict) -> None:
        sorted_entries = sorted(people.values(), key=self.get_birth_date)
        for entry in sorted_entries:
            print(f"{entry['name']} is a great scientist born in {entry['date_of_birth']}.")


women_scientists = {
 "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
 "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
 "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
 "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
 }

famous_births = FamousBirth().famous_births()
famous_births(women_scientists)