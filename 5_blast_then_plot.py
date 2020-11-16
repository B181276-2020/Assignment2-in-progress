#!/usr/bin/python3

#Synposis: Two functions. the first takes the the input .fasta sequence from the edirect section and outputs an alignment using the blastx command. The second function takes the alignment created and applies a plotcon to it to plot the alignment.

#Function 1:
#Input : proteinseq.fasta (the output of the efetch conducted)
#Process : run a blastx on the fasta file
#Output : seq_alignment.out (aligned protein sequence ready for further analysis)
import os
import shutil
import subprocess

print("Imported os, subprocess and shutil.")

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


#Website suggested this to run the blast: blastx -db ~/path/to/your/myformattedDBname/ -outfmt 5 -evalue 1e-3 -word_size 3 -show_gis -num_alignments 20 -max_hsps 20 -num_threads 5 -out local_blast.xml -query myDNAsequenceTOblast.fasta
#Website said that spaces have to be replaced by | 
#WORKS
#for line in proteinseq:
#	proteinseq_write.write("|".join(line.split(" ")))

#proteinseq_write.close()
#print (proteinseq)
	
#Function 1:
	#It does do the blast, but with the current test sequence it says "no hits found"
def blastthis (fastafile):
	print ("generating database for the protein sequences. Please wait...")
	os.system ("makeblastdb -in proteinseq.fasta -input_type fasta -dbtype prot -parse_seqids -out sequencedb ")
	print ("Now aligning downloaded protein sequences. Please wait...") 
	os.system ("clustalo -i proteinseq.fasta -o seq_alignment.msf -v")
	alignment=open("seq_alignment.fasta").read()
	#print (alignment)
	print ("The blast alignment was completed. It can be found under protein_sequences/seq_alignment.msf")
	return alignment

#Running function 1:
blastthis(proteinseq)

#Function 2:
#Input : the seq_alignment.out file
#Process : plotcon
# Output : a lovely plotcon graph 

#THE SEARCH VARIABLE IS A NONE TYPE ASK FOR HELP ON THIS
def plotconthis (alignment):
	print ("Now plotting the conservation of sequences across the protein alignment...")
	search_info=open("search.txt").read().strip()
	search = print (search_info)
	print (search)
	plotcon_command= print ("plotcon -sequences seq_alignment.msf -winsize 12 -graph x11 -scorefile EBLOSUM62 -gtitle \"Conservation of sequences in",search+"\"")	
	plot = subprocess.call(plotcon_command)
	print ("The plot has been completed.")
	return plot

# Combining running function 2 with a little interactive decission tree.

def checkpoint3_function(checkpoint3):
	if checkpoint3 == "Y" or checkpoint3 == "y" or checkpoint3 == "Yes":
		print ("Plotting conservation, please wait...")
		check3 = "True"
	elif checkpoint3 =="n" or checkpoint3 =="N" or checkpoint3 == "No":
		print ("Okay. Terminating program.")
		exit ()
	else:
		print ("Please answer with y for yes, I want to plot the conservation, or n for no, I want to exit the program.")
		check3 == "False"
	return check3

check3 = checkpoint3_function(input("Would you like to plot the conservation of this alignment?(y/n)"))
if check3== "True" :
	alignment=open("seq_alignment.fasta").read()
	plotconthis(alignment)
elif check3 == "False":
	checkpoint3_function(input("Would you like to plot the conservation of this alignment?(y/n)"))
else:
	exit ()

