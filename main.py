# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:20:55 2024

@author: HP
"""
import csv
import matplotlib.pyplot as plt

def main(): 
    '''
    Day 1
    '''  
    ''' reading the file '''
    f = open("Emissions.csv", "r")
    data = csv.reader(f)
    
    
    ''' transforming the rows into dictionary '''
    # transforming every row into a key:value pair and add this pair to the main dictionary
    rows_d = {}
    for row in data:
        rows_d.update(dict([(row[0],row[1:])]))
    
    #day2(rows_d)
    #day3(rows_d)
    #day4(rows_d)
    day5(rows_d)
   
        
def day2(rows_d):
    
    '''
    Day2
    '''
    ''' Taking input from the user '''
    # Note: input shall not be changed to intger as it's a string in the dictionary
    year = input("Select a year to find statistics (1997 to 2010): ")
    
    
    ''' Extracting index of the year '''
    index = rows_d.get('CO2 per capita').index(year)
    
    
    ''' Creating the list of emission in year '''
    emission_list = []
    countries = []
    for key,value in rows_d.items():
        emission_list.append(float(value[index]))
        countries.append(key)
    
    emission_list.pop(0)
    countries.pop(0)
    
    
    ''' Performing the analysis '''
    # Get the country with minimum emission
    Min_num = min(emission_list)
    Min_index = emission_list.index(Min_num)
    Min_country = countries[Min_index]
    
    # Get the country with maximum emission
    Max_num = max(emission_list)
    Max_index = emission_list.index(Max_num)
    Max_country = countries[Max_index]
    
    # calculate the average emission for the year
    Average_num = sum(emission_list) / len(emission_list)
    
    # Printing the data in required format using formatted string
    print("In {}, countries with minimum and maximum CO2 emission levels were: [{}] and [{}] respectively. Average CO2 emissions in {} were {:.6f}".format(year, Min_country, Max_country, year, Average_num))

def day3(rows_d):
    '''
    Day3
    '''
    ''' Taking input from the user '''
    # First Leatter must be capital
    country = input("Select a country to visualize: ")
    print(country)
    
    ''' extracting the data '''
    # getting the years [x-axis data] 
    years = [float(i) for i in rows_d['CO2 per capita']]
    print(years)
    
    # getting the emmisions [y-axis data]
    emission_list = [float(i) for i in rows_d[country]]
    print(emission_list)


    ''' plotting '''
    # Create figure and axis objects
    fig, ax = plt.subplots()  

    # plotting data
    ax.plot(years, emission_list)
    
    # adding titles
    ax.set(title='Year vs Emissions in Capita',
           ylabel='Emissions in {}'.format(country),
           xlabel='Year'
           )
    
    # show plot
    plt.show()
    
def day4(rows_d):
    '''
    Day4   
    '''  
    ''' Taking input from the user '''
    # First Leatter must be capital
    countries = input("Write two comma-separated countries for which you want to visualize data: ")  # Mongolia, Montenegro
    countries_list = countries.split(', ')
    print(countries_list)
    country_1 = countries_list[0]
    country_2 = countries_list[1]
    print(country_1)
    
    ''' extracting the data '''
    # getting the years [x-axis data] 
    years = [float(i) for i in rows_d['CO2 per capita']]
    print(years)
    
    # getting the emmisions [y-axis data]
    emission_list_1 = [float(i) for i in rows_d[country_1]]
    emission_list_2 = [float(i) for i in rows_d[country_2]]
    print(emission_list_1, emission_list_2)


    ''' plotting '''
    # Create figure and axis objects
    fig, ax = plt.subplots()  

    # plotting data
    ax.plot(years, emission_list_1)
    ax.plot(years, emission_list_2)
    
    # adding titles
    ax.set(title='Year vs Emissions in Capita',
           ylabel='Emissions',
           xlabel='Year'
           )
    
    # addong legend
    ax.legend([country_1, country_2])
    
    # show plot
    plt.show()

def day5(rows_d):
    '''
    Day5   
    '''  
    ''' Taking input from the user '''
    countries_list = []
    while len(countries_list) != 3:
        
        # First Leatter must be capital
        countries = input("Write up to three comma-separated countries for which you want to extract data: ") 
        # Australia, Austria, Azerbaijan, Bahamas
        
        countries_list = countries.split(', ')
        print(countries_list)
        
        if len(countries_list) == 3:
            break
        else: 
            print("ERR: Sorry, at most 3 countries can be entered.") 
                
    # field names
    fields = ['CO2 per capita'] + rows_d['CO2 per capita']
    print(fields)

    # adding data rows of fields dictionary
    rows = [fields]
    for country in countries_list: 
        rows.append([country] + rows_d[country])
    print(rows)
 
    # name of csv file
    filename = "Emissions_subset.csv"
 
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
 
        # writing the fields
        csvwriter.writerows(rows)

    print("Data successfully extracted for countries {} saved into file Emissions_subset.csv".format(countries))

if __name__== "__main__":
    main()
    