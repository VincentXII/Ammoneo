import subprocess, sys, os, shutil, csv
def ammoneo():
	print("R - Read Reminder List")
	while True:
		main = input("> ")

		if main == "R":
			read = input("What List Would You Like To Read? ")
			f = open(read)
			reader = csv.reader(f)
			for row in reader:
				print(row)

ammoneo()