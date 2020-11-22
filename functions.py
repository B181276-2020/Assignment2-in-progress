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
	os.system (system_call)
	alignment=open("seq_alignment_clustalo.msf").read()
	print ("The clustal omega alignment was completed. It can be found under output_data/seq_alignment_clustalo.msf")
	return system_call

#Feeds a file into plotcon command and runs it with a os.system call. Returns to the user interface at the end
def plotconthis (alignment,subtitle):
	import os, shutil, subprocess
	print ("Now plotting the conservation of sequences across the protein alignment...")
	#search_info=open("search.txt").read()
	plot="plotcon -sequences "+alignment+" -winsize 12 -graph x11 -scorefile EBLOSUM62 -gsubtitle \""+subtitle+"\" > conservation_plot.png"
	print ("The plot can be found under output_data/conservation_plot.png")
	os.system (str(plot))
	print ("The plot can be found under output_data/conservation_plot.png.\n Press enter to continue...")
	continuing = input("")
	os.chdir("..")
	os.system ("pwd")
	os.system ("python3 0_interface.py")
	return plot

#Creating an alignment file suitable for publication
#Feeds a inputfile determined by the user into a command and runs it using a os system call
def showalignthis (inputfile,outfile):
	import os, shutil, subprocess
	#Creates a string using the input for inputfile and outfile, to make a system call to run a showalign emboss. 
	#This generates a very pretty alignment file that can be used for a publication
	showalign_call = "showalign -sequence "+inputfile+" -outfile "+outfile
	print (showalign_call)
	os.system(showalign_call)
	print ("\n\nAn alignment suitable for publication was generated!\n It can be found under outputdata/"+outfile+" .")
	#copyover = "output_data/"+outfile
	#shutil.copy(outfile, copyover)
	return showalign_call

#Generating a consensus sequence:
#Feeds a inputfile determined by the user into a command and runs it using a os system call
def consthis (inputfile,outfile):
	import os, shutil, subprocess
	#Creates two strings, using the input for inputfile and outfile, to make a system call to run a con emboss, generating a consensus sequence for a set of aligned sequences 
	cons_call = "cons -sequence "+inputfile+" -outseq "+outfile
	print (cons_call)
	os.system(cons_call)
	print ("\n\nA consensus sequence for your alignment file was generated!\n It can be found under outputdata/"+outfile+" .")
	return cons_call

