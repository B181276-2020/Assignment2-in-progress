#!/usr/bin/python3


#				Synopsis:
#This will act as a "user interface" and allow the user to navigate the programmes.
import os,shutil
import importlib.util
# Have to import all the functions from my other scripts:
#from importlib.machinery import SourceFileLoader
from functions import *
#Imports functions from script 3
#spec = importlib.util.spec_from_file_location("3_efetch", "3_efetch.py")
#foo = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(foo)

#mymodule3 = SourceFileLoader("3_efetch","3_efetch.py").load_module()
#Imports functions from script 5
#mymodule5 = SourceFileLoader("5_blast_then_plot","5_blast_then_plot.py").load_module()
#Imports functions from script 9
#mymodule9 = SourceFileLoader("9_plotcon","9_plotcon.py").load_module()

os.system("clear")
if os.path.exists("protein_sequences"):
	print ("")
	#print ("protein sequences exist!")
else:
	os.mkdir("output_data")
print ("\t\t\tUSER INTERFACE\t\t\t")
print("Hello there. This is the user interface. \nBelow are all the programmes you can use. Please type the associated number of the program and press enter.\n")
execute=input("""1.Run all programs in order\n
2.Esearching for proteins in a taxonomic family on NCBI\n
3.Efetching sequences from NCBI\n
4.Align Sequences\n
5.Plotting conservation graphs\n
""")
if execute == "1":
	print("You selected 1. Press enter to continue...")
	input=""
	os.system("./master_script.sh")
	os.system("python3 0_interface.py")

elif execute == "2":
	print("You selected 2. Press enter to continue...")
	input=""
	os.system("python3 1_esearch.py")
	os.system("python3 2_evaluating_query.py")
	os.system("python3 0_interface.py")

elif execute == "3":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 3. You will need your own query keys and web env as input to run this efetch. If you would like to obtain these, please run option 1 instead. Would you like to continue anyway? (y/n)")
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

elif execute == "4":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 4. You will need your own downloaded .fasta file containing protein sequences. If you would like to generate one, please run option 1 instead. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
				exit()
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.system ("clear")
	input_1 = input("Please enter your protein sequence file name:\n")
	#imported 5_blast_then_input.py functions earler, now used here
	databasemaker(input_1)
	aligner(input_1)
	print ("Press enter to return to the user interface.")
	input = ""
	os.system("python3 0_interface.py")
#Plotcon option. Gives user the option to opt out and run the user interface again
elif execute == "5":
	print("\n")
	proceed = "check"
	while proceed not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("You selected 5. You will need your own aligned sequences in a file format compatible with plotcon (such as an .msf file). If you would like to generate such a file, please run option 1 instead. Would you like to continue anyway? (y/n)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				break
			elif answer_2 == ("no" or "No" or "N*"):
				os.system("python3 0_interface.py")
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	os.chdir("output_data")	
	input_1 = input("Please enter the name of the file containing your alignments:\n")
	#imported 9_plotcon.py plotcon this module earler, now used it here
	plotconthis(input_1)
	print ("Press enter to return to the user interface.")
	input = ""
	os.system("python3 0_interface.py")

else:
	os.system("python3 0_interface.py")
	

