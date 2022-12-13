import numpy as np
import matplotlib.pyplot as plt
import math
 
class Country:
    ''' A class used to create a Country object.
 
        Attributes:
            country (str): String that represents the country name
            UN_region (str): String that represents the region name
            UN_sub_region (str): String that represents the sub region name
            sq_KM (str): String that represents the size of the country in sq km
            plants (int): Integer that represents the amount of plants threatened
            fish (int): Integer that represents the amount of fish threatened
            birds (int): Integer that represents the amount of birds threatened
            mammals (int): Integer that represents the amount of mammals threatened
    '''
    def __init__(self, country, UN_region, UN_sub_region, sq_KM, plants, fish, birds, mammals):
        self.country = country
        self.UN_region = UN_region
        self.UN_sub_region = UN_sub_region
        self.sq_KM = sq_KM
        self.plants = plants
        self.fish = fish
        self.birds = birds
        self.mammals = mammals
 
   
    def print_country_data(self):
        ''' A function that prints the country name, region, sub region, and size of the country in sq KM.
       
        Parameters: None
        Return: None
 
        '''
        print("{} is in UN region, {}, in sub-region, {}. The size of {} is {} sq km.".format(self.country, self.UN_region, self.UN_sub_region, self.country, self.sq_KM))
 
    def print_threatened_species(self):
        ''' A function that prints the threatened species in the given country.
       
        Parameters: None
        Return: None
       
        '''
        print("There are {} threatened plant species, {} threatened fish species, {} threatened bird species, {} threatened mammal species in {}.".format(self.plants, self.fish, self.birds, self.mammals, self.country))
        print("The total numbers of threatened species is: {}".format(self.plants + self.fish + self.birds + self.mammals))
 
def find_countries(user_input, user_list, country_list):
    ''' A function that finds the country based on the user input, which can be from country name/ region/ sub region/ sq km.
        if user input results in duplicate region/ sub region/ sq km, a list of the given countries based on these options will be provided,
        that is used to further narrow down the country.
   
    Parameters: user_input(str), user_list(list), country_list(list)
    Return: row_index
    '''
    indices = []
    narrowed_country_list = []
    for row_index in range(len(user_list)): # Creates an array with index numbers that map to specific countries
        if user_input == user_list[row_index]:
            indices.append(row_index)

    if len(indices) == 1: # If user input refers to a specific country
        row_index = user_list.index(user_input)
        return row_index # Index of the row of the numpy array is returned
   
    else: # If user input (region, sub-region, sq km) refers to multiple countries
        if user_input.isnumeric() == True: # If user input is number (sq km)
            print("These are the countries with the size of {} sq km:".format(user_input))
            for element in indices:
                print(country_list[element], end = "    ")
        else: # If user input has alphabet characters or spaces
            print("These are the countries in {}:".format(user_input))
            for element in indices:
                print(country_list[element], end = "    ")
   
        for i in indices: # Creates a list of countries that are in the given region/sub-region/size in sq km
            narrowed_country_list.append(country_list[i])
   
        while (True): # Prompts user to pick a country in the given region/sub-region/size in sq km
            user_input = input("\nPlease enter one of the countries:\n")
            if user_input in narrowed_country_list:
                row_index = country_list.index(user_input)
                return row_index # Index of the row of the numpy array is returned
            else:
                print("Invalid input. Please try again.")
 
def create_species_graph(plants, fish, birds, mammals):
    '''A function that plots a bar graph for threatened species in the given country.
   
    Parameters: plants(int), fish(int), birds(int), mammals(int)
    Return: None
   
    '''
    plt.figure("Threatened Species")
    species_name = ["Plants", "Fish", "Birds", "Mammals"]
    num_species = [plants, fish, birds, mammals]
    plt.bar(species_name, num_species, color = ['green', 'blue', 'red', 'cyan'])
    plt.title("Threatened Species")
    plt.xlabel("Species")
    plt.ylabel("Number of Threatened Species")
    plt.show()
   
def create_population_graph(starting_year, ending_year, population_list):
    '''A function that plots a line graph of the change in population for the given country and years.
   
    Parameters: starting_year(int), ending_year(int), population_list(list)
    Return: None
    '''
    plt.figure("Population")
    years = list(range(starting_year, ending_year + 1))
    population = list()
    for i in years:
        index = i - 2000
        population.append(population_list[index])
    plt.plot(years, population)
    plt.xticks(years)
    plt.title("Population Over Time")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()
 
def main():
    # Numpy array data sets
    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', dtype = None, encoding = None)
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter = ',',  skip_header = True)
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True)
    # Lists created from country_data
    country_list = list(country_data[1:,0])
    UN_region_list = list(country_data[1:,1])
    UN_sub_region_list = list(country_data[1:,2])
    sq_KM_list = list(country_data[1:,3])
    while(True): # Finding country
        user_input= input("Please enter one of the following: country name, UN region, UN sub-region, land size in sq km:\n")
        if user_input in country_list: # User input is country name
            row_index = find_countries(user_input, country_list, country_list)
            break
   
        elif user_input in UN_region_list: # User input is region
            row_index = find_countries(user_input, UN_region_list, country_list)
            break
   
        elif user_input in UN_sub_region_list: # User input is sub region
            row_index = find_countries(user_input, UN_sub_region_list, country_list)
            break
        elif user_input in sq_KM_list: # User input is sq KM of the country
            row_index = find_countries(user_input, sq_KM_list, country_list)
            break
        else: # User input is invalid
            print("Invalid input. Please try again.")
   
    # Lists specific to a selected country created from population_data and threatened_species
    population_list = list(population_data[row_index][1:])
    threatened_species_list = list(threatened_species[row_index][1:])
   
    # Variables specific to a country
    country = country_list[row_index]
    UN_region = UN_region_list[row_index]
    UN_sub_region = UN_sub_region_list[row_index]
    sq_KM = sq_KM_list[row_index]
    plants = int(threatened_species_list[0])
    fish = int(threatened_species_list[1])
    birds = int(threatened_species_list[2])
    mammals = int(threatened_species_list[3])
   
    CountryClass = Country(country, UN_region, UN_sub_region, sq_KM, plants, fish, birds, mammals)
    CountryClass.print_country_data()
   
    while(True): # Point A (Main Menu)
        user_input = input("Choose one of the following:\n1. Statistics of population\t2. Statistics of threatened species\t3. End code\n")
        if user_input == "1": # Statistics of population
            while(True): # Point B
                user_input = input("Choose one of the following:\n1. Population of specific year\t2. The highest recorded population\t3. The lowest recorded population\n4. The average population between 2000-2020\t5. The change in population\n")
                if user_input == "1": # Population of specific year
                    while (True): # Point C
                        year = int(input("Enter year: "))
                        if year in range(2000, 2021):
                            column_index = year - 2000
                            print("The population of {} in {} is {}".format(country, year, int(population_list[column_index])))
                            break
                        else: # Invalid input. Sends user goes back to Point C
                            print("Invalid input. Please try again.")
                    break
                elif user_input == "2": # Highest population
                    pop_high = int(population_data[row_index][1:].max())
                    year = population_list.index(pop_high) + 2000
                    print("Highest recorded population is {} which was in the year {}".format(pop_high, year))
                    break
           
                elif user_input == "3": # Lowest population
                    pop_low = int(population_data[row_index][1:].min())
                    year = population_list.index(pop_low) + 2000
                    print("Lowest recorded population is {} which was in the year {}".format(pop_low, year))
                    break
       
                elif user_input == "4": # The average population
                    pop_average = int(population_data[row_index][1:].mean())
                    print("The average population of {} is {}".format(country, pop_average))
                    create_population_graph(2000, 2020, population_list) # Line graph
                    break
       
                elif user_input == "5": # The change in population
                    while(True): # Point D
                        starting_year = int(input("Please enter the starting year: "))
                        ending_year = int(input("Please enter the ending year: "))
                        if starting_year in range(2000, 2021) and ending_year in range(2000, 2021) and ending_year>starting_year:
                            starting_column_index = starting_year - 2000
                            ending_column_index = ending_year - 2000
                            starting_population = population_list[starting_column_index]
                            ending_population = population_list[ending_column_index]
                            change_in_population = (ending_population - starting_population)/(ending_year - starting_year)
                            print("The change in population from {} to {} is {} per year".format(starting_year, ending_year, round(change_in_population, 3)))
                            create_population_graph(starting_year, ending_year, population_list) # Line graph
                            break    
                        else: # User input is invalid. Sends user back to Point D
                            print("Invalid input. Please choose numbers from 2000-2020 and make sure ending year is greater than starting year")
                    break
                else: # User input is inavlid. Sends user back to Point B
                    print("Invalid input. Please try again.")
   
        # After running statistics of population, User is sent back to Point A (Main Menu)
   
        elif user_input == "2": # The threatened species of that country. Sends user back to Point A (Main Menu)
            CountryClass.print_threatened_species()
            create_species_graph(plants, fish, birds, mammals) # bar graph
        elif user_input == "3": # User terminates code. Exits loop
            print("Goodbye :)")
            break
        else: # User input is invalid. Sends user back to Point A (Main Menu)
            print("Invalid input. Please try again.")
   
if __name__ == '__main__':
    main()
