def cities_with_apollo_hospitals(filename):
    """Function to create a set of cities with at least one Apollo hospital."""
    apollo_cities = set()
    with open(filename, 'r') as file:
        for line in file:
            city, hospital = line.strip().split(',')
            if hospital.lower() == 'apollo':
                apollo_cities.add(city)
    return apollo_cities

filename = 'Dataset_Day1.csv'
apollo_cities =(filename)
print("Cities with at least one Apollo hospital:")
print(apollo_cities)


