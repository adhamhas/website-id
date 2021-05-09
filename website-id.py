#!/usr/bin/python3
import os 
os.system('sudo pip install builtwith --upgrade')
os.system('sudo pip install python-whois --upgrade')
import builtwith
import whois 
y =input("url: ")
x = builtwith.parse(y)
info = whois.whois(y)
print(x)
print(info)
