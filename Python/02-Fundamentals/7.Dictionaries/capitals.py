countries = input().split(", ")
capitals = input().split(", ")
country_capital = dict(zip(countries, capitals))

for k,v in country_capital.items():
    print(f"{k} -> {v}")
