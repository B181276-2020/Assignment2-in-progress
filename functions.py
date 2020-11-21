#!/usr/bin/python3
#				Synopsis:
#A collection of all the functions in the different scripts
import os, shutil, subprocess

#Function from script 3. Efetches using input
def downloadseq (query,web_env):
	import os, shutil, subprocess
	#Creates two strings, using the input for query and webenv, to make a 		 system call to run the bash wget command
	fasta_call = "wget -O proteinseq.fasta \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key="+query+"&WebEnv="+web_env+"&rettype=fasta&retmode=text\""
	print (fasta_call)
	genbank_call = "wget -O proteinseq_genbank.gb \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key="+query+"&WebEnv="+web_env+"&rettype=gb&retmode=text\""
	os.system(fasta_call)
	os.system(genbank_call)
	print ("\n\nThe protein sequences were downloaded! Two versions of the files exist, one in fasta format, the other in genbank format. The files can be found under output_data/proteinseq.fasta and output_data/proteinseq_genbank.gb respectively")
	shutil.copy("proteinseq.fasta", "output_data/proteinseq.fasta")
	shutil.copy("proteinseq.fasta", "output_data/proteinseq_genbank.gb")
	return fasta_call,genbank_call

#Functions from script 5:
#Generates a blast db using input
def databasemaker (fastafile):
	print ("generating database for the protein sequences. Please wait...")

	#This generates a string that allows a system call to run makeblastdb
	system_call = "makeblastdb -in "+fastafile+" -input_type fasta -dbtype prot -parse_seqids -out sequencedb "
	os.system (system_call)
	#os.system ("makeblastdb -in proteinseq.fasta -input_type fasta -dbtype prot -parse_seqids -out sequencedb ")
	return system_call

#Aligns fasta files using input
def aligner (fastafile):
	import os, shutil, subprocess
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

#Feeds a file into plotcon
def plotconthis (alignment):
	import os, shutil, subprocess
	print ("Now plotting the conservation of sequences across the protein alignment...")
	search_info=open("search.txt").read()
	plot="plotcon -sequences "+alignment+" -winsize 12 -graph x11 -scorefile EBLOSUM62 -gsubtitle \""+search_info+"\" > conservation_plot.png"
	#KICKS ME OUT HERE, MIGHT HAVE TO WRITE A SCRIPT OUTSIDE OF THIS TO CONTINUE THE PROGRAM
	print ("The plot can be found under output_data/conservation_plot.png")
	#print (plot)	
	os.system (str(plot))
