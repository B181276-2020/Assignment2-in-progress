#!/usr/bin/python3
#				Synopsis:
#A function for plotconning an input.

#SHOULD ADD AN OPTION FOR THE USER TO USE THESE FUNCTIONS WITH THEIR OWN FASTA FILES IF THEY WISH MAYBE
import os, sys, shutil
os.system("clear")
os.chdir("protein_sequences")

def plotconthis (alignment):
	print ("Now plotting the conservation of sequences across the protein alignment...")
	search_info=open("search.txt").read()
	plot="plotcon -sequences "+alignment+" -winsize 12 -graph x11 -scorefile EBLOSUM62 -gsubtitle \""+search_info+"\" > user_plot.png"
	#KICKS ME OUT HERE, MIGHT HAVE TO WRITE A SCRIPT OUTSIDE OF THIS TO CONTINUE THE PROGRAM
	print ("The plot can be found under protein_sequences/user_plot.png")
	#print (plot)	
	os.system (str(plot))
	return plot

# Combining running function 2 with a little interactive decission tree.

user_answer = ""
while user_answer not in ("yes", "Yes", "Y*", "no", "No", "N*"):
	user_answer = input("Would you like to plot the conservation of the best 250 alignments?(yes/no). \n (Your plot can be found under protein_seqeunces/user_plot.png\n")
	if user_answer == ("yes" or "Yes" or "Y*"):
		print("Plotting Conservation, please wait...")
		
		alignment="seq_alignment_250.msf"
		plotconthis(alignment)
		alignment="seq_alignment_clustalo.msf"
		plotconthis(alignment)
		break
	elif user_answer == ("no" or "No" or "N*"):
		print("You selected no.");
		#For now:
		break
		#DECIDE WHAT TO DO HERE!!
		#os.system("./master_script.sh") ;
		#Could execute a selection script of sorts here for other options
	else:
		print("Please answer with yes for \" I want to plot the conservation \", or no for \"I want to exit the program.\"\n")

