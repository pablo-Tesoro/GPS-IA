
import csv 
btns = []
with open('coordImg.csv', 'r') as File:  
    reader =csv.reader(File, delimiter=';')
    for row in (reader) :
        print(row)