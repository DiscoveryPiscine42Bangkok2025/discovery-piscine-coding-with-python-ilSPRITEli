original = [2, 8, 9, 48, 8, 22, -12, 2]
processed = {value + 2 for value in original if value > 5}

print(f"Original array: {original}")
print(f"New array: {processed}")


