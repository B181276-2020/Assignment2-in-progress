#!/usr/bin/python3
#				Synopsis:
#A short case version of a while statement to allow the user to delete the proteinseq.fasta file and interrupt the program. Re-runs the whole program if the user chooses to delete the file.
import os
os.system("clear")

proceed = "check"
proceed_2 = "check"
while proceed not in ("yes", "Yes", "Y", "y" "no", "No", "N"):
	answer = input("Would you like to continue? \nIf you answer with yes then the program will continue to aligning the sequences. \nIf you select no, the sequences will be deleted and you will be directed to the user interface.(yes/no)")
	if answer == ("yes" or "Yes" or "Y" or "y"):
		fasta = open("proteinseq.fasta").read()
		print ("Continuing to analysis...")
		break
	elif answer == ("no" or "No" or "N" or "n"):
		#This removes all the protein sequence files and takes the user back to the user interface
		print("You selected no.\n")
		print("Deleting results of esearch and efetch now...")
		#os.remove("proteinseq.fasta")
		os.remove("proteinseq_genbank.gb")
		#os.remove("output_data/proteinseq.fasta")
		#os.remove("output_data/proteinseq_genbank.gb")
		print("Files have been removed.\nPress enter to continue...")
		input("")
		os.system("python3 0_interface.py")
		exit()
	else:
		print ("Please answer with y for yes, or n for no.\n\n")

