# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:20:55 2024

@author: HP
"""
import csv

def main(): 
    
    # reading the file
    f = open("Emissions.csv", "r")
    data = csv.reader(f)
    
    # transforming the rows into dictionaries & storing them in a list
    rows_d = {}
    for row in data:
        row_d = dict([(row[0],row[1:])])
        #print(*[str(k) + ':' + str(v) for k,v in row_d.items()])
        
        rows_d.update(row_d)
        #print(rows_d)
    # Taking input from the user
    # Note: input shall not be changed to int as it's a string in the dictionary
    year = input("Select a year to find statistics (1997 to 2010): ")
    print(year)
    
    # Extracting index of the year
    index = rows_d.get('CO2 per capita').index(year)
    print(index)
    
    # Creating the list of emission in year
    emission_list = []
    countries = []
    for key,value in rows_d.items():
        emission_list.append(float(value[index]))
        countries.append(key)
     
    emission_list.pop(0)
    countries.pop(0)

    print(emission_list)
    
    # Performing the analysis
    Min_num = min(emission_list)
    Min_index = emission_list.index(Min_num)
    Min_country = countries[Min_index]
    
    Max_num = max(emission_list)
    Max_index = emission_list.index(Max_num)
    Max_country = countries[Max_index]
    
    
    
    Average_num = sum(emission_list) / len(emission_list)
    
    print("In {}, countries with minimum and maximum CO2 emission levels were: [{}] and [{}] respectively. Average CO2 emissions in {} were {:.6f}".format(year, Min_country, Max_country, year, Average_num))
    
    # Printing the data in required format using formatted string
    








if __name__== "__main__":
    main()
    