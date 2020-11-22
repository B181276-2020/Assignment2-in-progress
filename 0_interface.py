#!/usr/bin/python3


#				Synopsis:
#This will act as a "user interface" and allow the user to navigate the programmes.
import os,shutil
import importlib.util
# Have to import all the functions from my other scripts. They are located in a file called functions.py
from functions import *

#Creates the output file directory:
os.system("clear")
if os.path.exists("output_data"):
	print ("")
	#print ("protein sequences exist!")
else:
	os.mkdir("output_data")

#Shows the user interface:
print ("\t\t\t\tUSER INTERFACE\t\t\t")
print("Hello there. This is the user interface. \nBelow are all the programmes you can use. Please type the associated number of the program and press enter.\n")
execute=input("""FUNCTIONALITIES:\n\n1.Run all programs in order\n
2.Esearching for proteins in a taxonomic family on NCBI\n
3.Efetching sequences from NCBI\n
4.Align Sequences\n
5.Plotting conservation graphs\n\n
NOT PART OF OPTION 1, EXTRA FUNCTIONALITIES:\n
6. Generate an alignment file suitable for publication \n
7. Generate a consensus sequence for an alignment file \n\n
EXIT OPTIONS:\n
8. Exit and take me to the output_data directory\n
9. Exit\n
""")
#Running the user interface with the input "execute"
#Option 1: Runs the standard selection of programs from top to bottom
if execute == "1":
	print("You selected 1. Press enter to continue...")
	input=""
	os.system("./master_script.sh")
	os.system("python3 0_interface.py")
#Option 2: Runs only the esearch and evaluation of the esearch
elif execute == "2":
	print("You selected 2. Press enter to continue...")
	input=""
	os.system("python3 1_esearch.py")
	os.system("python3 2_evaluating_query.py")
	os.system("python3 0_interface.py")
#Option 3: Runs an efetch using user input. Has an interactive section built in
elif execute == "3":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 3. \nYou will need your own query keys and web env as input to run this efetch. If you would like to obtain these, please run option 1 instead. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
				exit()
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	#imported 3_efetch.py functions earlier, now can use the download function seperately
	os.system("clear")
	input_1 = input("Please enter your query key:\n")
	input_2 = input("Please enter your webenv:\n")
	downloadseq(input_1,input_2)
	print("\nYour efetch was complete, your files will be saved under proteinseq.fasta and proteinseq_genbank.gb, respectively, in the current directory.\n\n Press enter to return to the user interface.")
	input("")
	os.system("python3 0_interface.py")
#Option 4: Runs an alignment using user input. Has an interactive section built in
elif execute == "4":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 4. \nYou will need your own downloaded .fasta file containing protein sequences located in the output_data directory. If you would like to generate one, please run option 1 instead. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
				exit()
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.system ("clear")
	input_1 = input("Please enter your protein sequence file name:\n")
	#imported functions earlier, now used here
	databasemaker(input_1)
	aligner(input_1)
	print ("Press enter to return to the user interface.")
	input = ""
	os.system("python3 0_interface.py")
#Option 5: Plotcon using user input, gives user the option to opt out and run the user interface again
elif execute == "5":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 5. \nYou will need your own aligned sequences in a file format compatible with plotcon (such as an .msf file). If you would like to generate such a file, please run option 1 instead. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.chdir("output_data")	
	input_1 = input("Please enter the name of the file containing your alignments:\n")
	input_1 = input("Please enter the subtitle you would like to write under the title of the graph:\n")
	#imported 9_plotcon.py plotcon this module earler, now used it here
	plotconthis(input_1,input_2)
	print ("Press enter to return to the user interface.")
	input = ""
	os.system("python3 0_interface.py")
#Option 6: (extra functionality) Generates a file containing the alignments, but it is organised and suitable for publication. Has an interactive bit built in
elif execute == "6":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 6. \nYou will need a alignment file name that corresponds to a suitable file containing alignments, located in the output_data directory (such as an .msf file). If you would like to generate such a file, please run option 1 first. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.chdir("output_data")	
	input_1 = input("Please enter the name of the file containing your alignments:\n")
	input_2 = input("Please enter what you would like your output file to be called. It will be located in the output_data directory after the program finished:\n")
	showalignthis(input_1,input_2)
	next= input("Press enter to return to the user interface.")
	os.chdir("..")
	os.system ("pwd")
	os.system ("python3 0_interface.py")

#Option 7: (extra functionality) Compiles a consensus sequence using an input file determined by the user
elif execute == "7":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 7. You will need a alignment file name that corresponds to a suitable file containing alignments, located in the output_data directory (such as an .msf file). If you would like to generate such a file, please run option 1 first. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.chdir("output_data")	
	input_1 = input("Please enter the name of the file containing your alignments:\n")
	input_2 = input("Please enter what you would like your output file to be called. It will be located in the output_data directory after the program finished:\n")
	consthis(input_1,input_2)
	next= input("Press enter to return to the user interface.")
	os.chdir("..")
	os.system ("pwd")
	os.system ("python3 0_interface.py")
elif execute == "8":
	os.chdir("output_data")
	os.system("ls")
	exit()
elif execute == "9":
	exit ()
else:
	os.system("python3 0_interface.py")
	

