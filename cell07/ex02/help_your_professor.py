class Avg:
    def average(self, scores_dict: dict) -> float:
        if not scores_dict:
            return 0.0
        total = sum(scores_dict.values())
        return total / len(scores_dict)


class_3B = {
 "marine": 18,
 "jean": 15,
 "coline": 8,
 "luc": 9
 }
class_3C = {
 "quentin": 17,
 "julie": 15,
 "marc": 8,
 "stephanie": 13
}

avg = Avg()
print(f"Average for class 3B: {avg.average(class_3B)}.")
print(f"Average for class 3C: {avg.average(class_3C)}.")