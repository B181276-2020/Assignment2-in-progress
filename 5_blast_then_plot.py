#!/usr/bin/python3

#Synposis: Two functions. the first takes the the input .fasta sequence from the edirect section and outputs an alignment using the blastx command. The second function takes the alignment created and applies a plotcon to it to plot the alignment.

import os
import shutil
import subprocess
os.system("clear")
print("Imported os, subprocess and shutil.\n\n")

#This is for titling the plot later:
shutil.copy("search.txt", "protein_sequences/search.txt")

#First we get the proteinseq.fasta file to the right directory
	#WORKS! HASHED TO PREVENT ERROR
#os.rename ("proteinseq.fasta","protein_sequences/proteinseq.fasta")
#This instead copies it for now
shutil.copy("proteinseq.fasta", "protein_sequences/proteinseq.fasta")
os.chdir ("protein_sequences")
#os.getcwd()
#Open the file connections. Need one for reading and the other for modifying the file
proteinseq=open("proteinseq.fasta").read()
#proteinseq_write=open("proteinseq.fasta","wt")


#Function 1:
	#Input	: the .fasta file. 
	#Process: Make a databse for the sequence alignment and then generate a 		  sequence alignment using clustalo
	#Output : a sequence alignment.msf file that can be accepted by clustalo
def blastthis (fastafile):
	print ("generating database for the protein sequences. Please wait...")
	os.system ("makeblastdb -in proteinseq.fasta -input_type fasta -dbtype prot -parse_seqids -out sequencedb ")
	print ("Now aligning downloaded protein sequences. Please wait...") 
	os.system ("clustalo -i proteinseq.fasta -o seq_alignment_clustalo.msf -maxnumseq=250 -v")
	#
	alignment=open("seq_alignment_clustalo.msf").read()
	#print (alignment)
	#os.system("clear")
	print ("The blast alignment was completed. It can be found under protein_sequences/seq_alignment_clustalo.msf")
	return alignment

#Running function 1:
blastthis(proteinseq)

#Function 2:
#Input	 : the seq_alignment.out file
#Process : plotcon
#Output  : a lovely plotcon graph 

def plotconthis (alignment):
	print ("Now plotting the conservation of sequences across the protein alignment...")
	search_info=open("search.txt").read()
	plot="plotcon -sequences seq_alignment_clustalo.msf -winsize 12 -graph x11 -scorefile EBLOSUM62 -gsubtitle \""+search_info+"\" > user_plot.png"
	#KICKS ME OUT HERE, MIGHT HAVE TO WRITE A SCRIPT OUTSIDE OF THIS TO CONTINUE THE PROGRAM
	print ("The plot can be found under protein_sequences/user_plot.png")
	#print (plot)	
	os.system (str(plot))
	return plot

# Combining running function 2 with a little interactive decission tree.

user_answer = ""
while user_answer not in ("yes", "Yes", "Y*", "no", "No", "N*"):
	user_answer = input("Would you like to plot the conservation of this alignment?(yes/no).")
	if user_answer == ("yes" or "Yes" or "Y*"):
		print("Plotting Conservation, please wait...")
		alignment=open("seq_alignment_clustalo.msf").read()
		user_plot = plotconthis(alignment)
		user_plot
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

#Old interactive bit, had bugs:
	
#check3 = checkpoint3_function(input("Would you like to plot the conservation of this alignment?(y/n)"))
#if check3== "True" :
#	alignment=open("seq_alignment.fasta").read()
#	plotconthis(alignment)
#elif check3 == "False":
#	checkpoint3_function(input("Would you like to plot the conservation of this alignment?(y/n)"))
#else:
#	exit ()
#def checkpoint3_function(checkpoint3):
#	check = "False"
#	if checkpoint3 == "Y" or checkpoint3 == "y" or checkpoint3 == "Yes":
#		print ("Plotting conservation, please wait...")
#		check3 = "True"
#	elif checkpoint3 =="n" or checkpoint3 =="N" or checkpoint3 == "No":
#		print ("Okay. Terminating program.")
#		exit ()
#	else:
#		print ("Please answer with y for yes, I want to plot the conservation, or n for no, I want to exit the program.")
#		check3 == "False"
#	return check3
