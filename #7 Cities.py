#7 Cities

cities = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]
    
for item in cities:
    item = list(item)

population = sum(pop for city, pop  in cities)
nb_of_cities = len(cities)

def sort_key(item):
    return item[1]

cities_sorted = sorted(cities, key=sort_key)

print(cities_sorted)
print(f'Sum of citizens in 10 cities is :{population}')
print(f'Average in 10 cities is : {(population)/(nb_of_cities)}')
