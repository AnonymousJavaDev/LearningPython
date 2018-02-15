#!/usr/bin/env python
# -*- coding: UTF-8 -*-

name = raw_input("What is your name? :")
age = input("How old are you (in years)? :")

print "Hello " + name
print "You are", age,
print "years old"

print "You will be 100 years old in the year: ", 2017 - age + 100

print "\n\n\n"
copies = input("How many times do you want me to print that out? : ")

inverse_copies = copies
while copies > 0:
    copies = copies - 1
    print inverse_copies - copies, ": You will be 100 years old in the year: ", 2017 - age + 100

