#!/usr/bin/python3
#Gorkem Sayilgan 
#This is just a simple script to do simple recon on a target url. You would use more professional tools but anyways.
#Tested on ParrotOS 4.9 Security Mate on 6/8/2020 
import requests
import urllib.request
from bs4 import BeautifulSoup
print("Just a simple script to do simple recon on a target url. You would use more professional tools but anyways.")
url = input("Enter the url you want to work with, example: https://google.com: ===> ")
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
key = ''
while key != '0':
    print("\n---------------------------------------------------------------------------------------------\n")
    print("Press 1 to see the header code like 200,403,404 ...")
    print("Press 2 to parse the html in a pretty way.")
    print("Press 3 to get the title.")
    print("Press 4 to get all the text.")
    print("Press 5 to get all links within <a> tags")
    print("Press 6 to get header values such as cookie")
    print("Press 0 to exit the program")
    print("1 and 6 have some authentication issues due to a spesific function, works well on sites like google, yahoo, github etc.\nI could not find a work around yet.")
    key = input("Your choice?: ")
    print("\n---------------------------------------------------------------------------------------------\n")
    
    if key == '1' :
        try:
            r1 = urllib.request.urlopen(url)
            print(r1.code)
        except:
            print("Encountered authentication error")        
       
    elif key == '2' :
        print(soup.prettify())
        
    elif key == '3' :
        print(soup.title)
        
    elif key == '4' :
        print(soup.get_text())
        
    elif key == '5' :
        for link in soup.find_all('a'):
            print(link.get('href'))
    
    elif key == '6' :
        try:
            r1 = urllib.request.urlopen(url)
            for header, value in r1.headers.items():
                print(header+" : "+value)
        except:
            print("Encountered authentication error")    
    elif key == '0' :
        print("See you later...")
    else :
        print("Please only enter the numbers above")




















