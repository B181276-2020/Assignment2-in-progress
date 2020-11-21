#!/usr/bin/python3

#				Synposis: 
#Two functions:
#1. Takes the the input .fasta sequence from the edirect section and outputs an alignment using the blastx command. 

#2. Takes the alignment created and applies a plotcon to it to plot the alignment.

import os
import shutil
import subprocess
os.system("clear")
print("Imported os, subprocess and shutil.\n\n")

#This is for titling the plot later:
shutil.copy("search.txt", "output_data/search.txt")

#First we get the proteinseq.fasta file to the right directory
	
shutil.copy("proteinseq.fasta", "output_data/proteinseq.fasta")
shutil.copy("proteinseq.fasta", "output_data/proteinseq_genbank.gb")
os.chdir ("output_data")


#Open the file connections. Need one for reading and the other for modifying the file
proteinseq=open("proteinseq.fasta").read()
#proteinseq_write=open("proteinseq.fasta","wt")


#Function 1:
	#Input	: the .fasta file. 
	#Process: Make a databse for the sequence alignment and then generate a 		  sequence alignment using clustalo
	#Output : a sequence alignment.msf file that can be accepted by clustalo

def databasemaker (fastafile):
	print ("generating database for the protein sequences. Please wait...")

	#This generates a string that allows a system call to run makeblastdb
	system_call = "makeblastdb -in "+fastafile+" -input_type fasta -dbtype prot -parse_seqids -out sequencedb "
	os.system (system_call)
	#os.system ("makeblastdb -in proteinseq.fasta -input_type fasta -dbtype prot -parse_seqids -out sequencedb ")
	return system_call

#Running function 1
fasta_file = "proteinseq.fasta"
databasemaker(fasta_file)

#Trying out different alignment options for blast
	#os.system ("blastp -db sequencedb -query proteinseq.fasta -out blast_alignment_format_6.out -outfmt 6")
	#os.system ("blastp -db sequencedb -query proteinseq.fasta -out blast_alignment_format_8.out -outfmt 8")
	#THIS ONE IS VERY GOOD FOR GENERATING A .msf FILE!!


#Function 2:
	#Input	: the .fasta file. 
	#Process: Generate a sequence alignment using clustalo, creating a .msf 		  file
	#Output : a sequence alignment.msf file that can be accepted by plotcon

def aligner (fastafile):
	print ("Now aligning downloaded protein sequences. Please wait...")
	#This aligns all the sequences in order of best alignment to worst alignment, based on an algorithm processed by clustalo 
	system_call = "clustalo -i "+fastafile+" -o seq_alignment_clustalo.msf --output-order tree-order --force -v"
	#os.system ("clustalo -i proteinseq.fasta -o seq_alignment_clustalo.msf --output-order tree-order --force -v")
	os.system (system_call)
	alignment=open("seq_alignment_clustalo.msf").read()
	#print (alignment)
	#os.system("clear")
	print ("The clustal omega alignment was completed. It can be found under output_data/seq_alignment_clustalo.msf")
	return system_call

#Running function 2:
aligner(fasta_file)


