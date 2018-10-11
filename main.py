import subprocess, sys, os, shutil, csv
def ammoneo():
	print("R - Read Reminder List")
	print("N - New Reminder List")
	print("X - Exit")
	while True:
		main = input("> ")

		if main == "R":
			read = input("What List Would You Like To Read? ")
			f = open(read)
			reader = csv.reader(f)
			for row in reader:
				print (','.join(row))

		if main == "N":
			new = input("Name of New List: ")
			firstremind = input("First Reminder: ")
			with open(new, 'wb') as csvfile:
				filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow([firstremind])
			#write = input("Name of New List: ")
			#ifile  = open(write, "rb")
			#reader = csv.reader(write)
			#ofile  = open(write, "wb")
			#writer = csv.writer(ofile, quotechar='"', quoting=csv.QUOTE_ALL)
			#for row in reader:
			#	writer.writerow(row)
			#	ifile.close()
			#	ofile.close()


		if main == "X":
			exit()

		else:
			ammoneo()

ammoneo()