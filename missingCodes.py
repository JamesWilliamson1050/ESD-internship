# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:05:23 2021

@author: Morrison
"""
import csv

with open('missingCodes.csv', 'w', encoding="utf-8", newline='\n') as csvfile:

    toWrite = csv.writer(csvfile)
    
    
    
    with open("moduleInfo2codes.csv", 'r', encoding='utf-8') as csv_file:
                    #reader = csv.DictReader.(csv_file)
        reader = csv.reader(csv_file)
                    
        for row in reader: 
            #print(row)            
            #print(type(reader))
            if len(row[0].strip()) == 0:
                toWrite.writerow([row[0], row[1]])
                
            

            

    
        