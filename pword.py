#!/usr/bin/env python3
#This is just importing the randomizer for the generator.
import random

#This is intro of the generator and when you press enter it moves on to what's your number.
input("Welcome to my password generator. Press enter to continue")

upperletters = ["A", "B," "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
char = ["!","@","#","$","%","^","&","*","(","-","_","+",")"]
password = []

#This is explaining when you enter your length choice it adds the two arrows. This appears before your password. It also prints a question and then it inputs the number in the generator.
print("How many characters do you want your password to be?")
lengthchoice = input(">>")
length = int(lengthchoice)

#This is making the generator the range is choosing from how many letters to the amount you insert. It's also randomizing your password.
for generator in range(0, length):
	lists = (upperletters, lowerletters, numbers, char)
	characterchoice = random.choice(lists)
	active = random.choice(characterchoice)
	pas = random.choice(list(active)) 
	password.append(pas) 
	
print("".join(map(str,password))) #This makes the password print obviously and it joins all the letters into one string.
