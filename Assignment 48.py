# read the file country data and find total population for continent using list
# and function.

country_path = r"C:\Users\Ganseh\Desktop\Python Assignments\SQL FILES\countrydata.csv"

country_list = []
count = -1
#print("opening countrydata file")
for row in open(country_path):
    # skipping the first row
    if count == -1:
        count += 1
        continue
    # extracting the data in rows
    id, country, continent, population, life_expectancy, gdp_per_cap = row.strip().split(",")
    population = float(population)# converting id to integers from str
    flag = True
    for idx in range(len(country_list)):
        if country_list[idx][0] == continent:
            flag = False
            country_list[idx] = (continent,country_list[idx][1]+population)
    if(flag):
        country_list.append((continent,population))
print(country_list)
