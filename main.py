import subprocess, sys, os, shutil, csv
def ammoneo():
	print("R - Read Reminder List")
	print("N - New Reminder List")
	print("X - Exit")
	while True:
		main = input("> ")

		if main == "R":
			read = input("What List Would You Like To Read? ")
			read = read + ".vtdl"
			f = open(read, 'r')
			reader = csv.reader(f)
			for row in reader:
				print (','.join(row))

		if main == "N":
			new = input("Name of New List: ")
			new = new + ".vtdl"
			firstremind = input("First Reminder: ")
			with open(new, 'w') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([firstremind])


		if main == "X":
			exit()

		else:
			ammoneo()

ammoneo()