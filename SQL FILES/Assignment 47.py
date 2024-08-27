# read the file country data and find total population for continent using dict and function


country_path = r"C:\Users\Ganseh\Desktop\Python Assignments\SQL FILES\countrydata.csv"

country_dict = {}
count = -1
#print("opening countrydata file")
for row in open(country_path):
    # skipping the first row
    if count == -1:
        count += 1
        continue
    # extracting the data in rows
    id, country, continent, population, life_expectancy, gdp_per_cap = row.strip().split(",")
    population = float(population)  # converting id to integers from str
    if continent not in country_dict:
        country_dict[continent]= population
    else:
        country_dict[continent] = population + country_dict[continent]

    #print("country_data")
print(country_dict)


