# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 10:20:55 2024

@author: HP
"""
import csv


def main(): 
    f = open("Emissions.csv", "r")
    data = csv.reader(f)
    for row in data:
        row_d = dict([(row[0],row[1:])])
        print(*[str(k) + ':' + str(v) for k,v in row_d.items()])








if __name__== "__main__":
    main()
    