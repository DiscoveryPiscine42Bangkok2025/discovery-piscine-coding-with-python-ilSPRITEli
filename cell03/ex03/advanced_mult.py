for table in range(11):
    line = [f"Table de {table}:"]
    for n in range(11):
        line.append(str(table * n))
    print(" ".join(line))


