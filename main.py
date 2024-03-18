# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:20:55 2024

@author: HP
"""
import csv

def main(): 
    
    ''' reading the file '''
    f = open("Emissions.csv", "r")
    data = csv.reader(f)
    
    
    ''' transforming the rows into dictionary '''
    # transforming every row into a key:value pair and add this pair to the main dictionary
    rows_d = {}
    for row in data:
        rows_d.update(dict([(row[0],row[1:])]))


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



if __name__== "__main__":
    main()
    