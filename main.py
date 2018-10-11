import subprocess, sys, os, shutil, csv
def ammoneo():
	print("R - Read Reminder List")
	while True:
		main = input("> ")

		if main == "R":
			read = input("What List would you like to Read?: ")	
			with open(read) as r:
				reader = csv.reader(r)
				for row in reader:
					print(row)

ammoneo()