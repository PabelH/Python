items = input("Please enter some countries separated by commas:\n")

countries = [country for country in items.split(",")]

print(",".join(sorted(list(set(countries)))))
