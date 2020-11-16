#!/usr/bin/python3

#Synposis: Two functions. the first takes the the input .fasta sequence from the edirect section and outputs an alignment using the blastx command. The second function takes the alignment created and applies a plotcon to it to plot the alignment.

#Function 1:
#Input : proteinseq.fasta (the output of the efetch conducted)
#Process : run a blastx on the fasta file
#Output : seq_alignment.out (aligned protein sequence ready for further analysis)
import os
import shutil


print("Imported os,shutil and ")

#First we get the proteinseq.fasta file to the right directory
	#WORKS! HASHED TO PREVENT ERROR
#os.rename ("proteinseq.fasta","protein_sequences/proteinseq.fasta")
os.chdir ("protein_sequences")
os.getcwd()
proteinseq=open("proteinseq.fasta").read()

#Function 1:
	#It does do the blast, but with the current test sequence it says "no hits found"
#Website suggested this to run the blast: blastx -db ~/path/to/your/myformattedDBname/ -outfmt 5 -evalue 1e-3 -word_size 3 -show_gis -num_alignments 20 -max_hsps 20 -num_threads 5 -out local_blast.xml -query myDNAsequenceTOblast.fasta
def blastthis (fastafile):
	print ("generating database for the protein sequences. Please wait...")
	os.system ("makeblastdb -dbtype prot -in proteinseq.fasta -parse_seqids -out proteindb")
	print ("Now aligning downloaded protein sequences. Please wait...")
	os.system ("blastx -db proteindb -query proteinseq.fasta -out seq_alignment.out")
	alignment=open("seq_alignment.out").read()
	print (alignment)
	print ("The blast alignment was completed.")
	return alignment

#blastthis(proteinseq)


#Function 2:
#Input : the seq_alignment.out file
#Process : plotcon
# Output : a lovely plotcon graph 

def plotconthis (alignment):
	print ("Now plotting the conservation of sequences acorss the protein alignment")
	

