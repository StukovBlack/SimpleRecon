#!/usr/bin/python3

import requests
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing


f = open("uniqlet.txt", "r")
f2 = open("uniqueones.txt", "w")    
lines = f.readlines()

for i in range(0, len(lines)):
    count = 0
    line1 = lines[i]
   
    try:
        r1 = requests.get(line1, verify=False)
    except:
        print("Error occured")
    soup1 = BeautifulSoup(r1.text, 'html.parser')
        
    for j in range(i,len(lines)-1):
        line2 = lines[j+1]
        try:
            r2 = requests.get(line2, verify=False)
        except:
            print("Error occured")
              
        soup2 = BeautifulSoup(r2.text, 'html.parser')
            
        if soup1 == soup2:
            count+=1
        
    if count == 0:
        print(line1 + "is unique")
        f2.write(line1)
f.close()            
f2.close()  
