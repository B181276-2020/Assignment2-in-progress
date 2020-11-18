#!/usr/bin/python3
#The alignment.txt file contains a multiple sequence alignment, one sequence per line. We want to draw a plot of protein conservation based on the alignment similarities, but without using plotcon!
import os, sys, shutil
import numpy as np
import matplotlib.pyplot as plt

os.chdir("protein_sequences")
alignment= open("seq_alignment_clustalo.msf")
aligned_seqs = []
counter = 0
counter_2 = 0
seqid_seq_dict={}
seqseq_id_dict={}
seq_headers = []
seq_only = []
align_list =[]
#This finds all sequence headers and puts them into a list
for line in alignment:
	counter_2 += 1
	if ">" in line:
		line_fixed=line.replace("\n","")
		seq_headers.append(line_fixed)
#print (seq_headers)

#This makes a list, where each alignment (including seq headers) are an element of the list
alignment= open("seq_alignment_clustalo.msf").read()
align_list=alignment.replace("\n","").split(">")


counter = 0
for element in align_list:
	starter = element.find("]")
	sequence = element[starter+1:]
	seq_only.append(sequence)
	counter = (counter + 1)

#print (seq_only)
counter = 0
#This fills the dict, where the keys are the headers of the sequences and the values are the alignments.
	#WORKS!
	#FOR seqseq_id_dict:
	#Key is the seqeunce
	#Header is the value
	#FOR seqid_seq_dict:
	#Header is the seqeunce
	#Key is the value

	#This is because the sequence is what both dictionaries have in common, and you cannot call a key using a value, which is important later
for header in seq_headers:
	seq = seq_only[counter]
	seqseq_id_dict[seq] = header
	seqid_seq_dict[header] = seq
	counter += 1


#print(seqid_seq_dict)
#This goes through each sequence in the dict. Then finds out how many uniques there are
uniquesincolumn = []
for seq in seqid_seq_dict.values():
	alignment_length = len(seq)
	column = []
	for column_number in range(alignment_length):
		aa = seq[column_number]
		if aa != "-":
			column.append(seq[column_number])
	#print (column)
	uniques = len((column))
	uniquesincolumn.append(uniques)
	
#print(uniquesincolumn)


#This creates a dictionary that has the headers of the seqeunces as keys and a corresponding score for these sequences.
#Currently the score is the length of the sequence minus the amount of unique amino acids found in that sequence.
seqid_score_dict = {}
counter = 0
#numbers_to_plot = []
for seq in seqid_seq_dict.values():
	seq_len = len(seq)
	aa = uniquesincolumn[counter]
		#print (aa)
	score = seq_len - aa
	#print (score)
	#header_list=seqid_seq_dict.keys()
	#print (header_list)
	header=seqseq_id_dict.get(seq)
	seqid_score_dict[header] = score
	counter += 1
print (seqid_score_dict)


#Write a code that takes user input for how many of the best sequences they want to use and then evaluate for the best sequences using the seqid_score_dict.
	#Then, grab each of the sequences with the header and write them to a new file
#print(len(uniquesincolumn))
#print(uniquesincolumn)

#for start in range(len(uniques_per_column) - window):
#	win = uniques_per_column[start:start+window]
#	score = sum(win) / len(win)
#	numbers_to_plot.append(score)

#for column_number in range(alignment_length):
#	column = []
#	for seq in aligned_seqs:
#		aa = seq[column_number]
#		if aa != "-":
#			column.append(seq[column_number])
#	uniques = len(set(column))
#	uniques_per_column.append(uniques)
#print (uniques_per_column)


#Code from excercise 2

	

#for header in seq_headers:
#	alignment.strip("\n")
#	alignmen.split(">")
#	print (alignment)
#	start = len(header)
#	for line in alignment:
#	print 
	
#This checks the length of the alignments. its 2013 consistently
#for lines in alignment:
#	counter += 0
#	end_of_id = alignment.find("]")
#	print("The id of seqeunce", counter, "was", alignment[0:end_of_id]+ "]")
	#print ("Sequence", counter_2, "was",len(line.rstrip("\n")),"long")
	#end_of_id=line.find("]")
	#print ("he id of seqeunce", counter_2, "was", line[0:end_of_id]+ "]")
	#aligned_seqs.append(line.rstrip("\n"))

#alignment_length = len(aligned_seqs[0])
#print ("This is the alignment length:"alignment_length)
#uniques_per_column = []

#This goes through each coloumn in each sequence and if the amino acid in that column is not a "-" it will add it to the list "column". It then makes a non redundant list of column, counts the amount and then adds the resulting "number of uniques" to a new list, each element in this new list representing the number of unique amino acids in each sequence.
#for column_number in range(alignment_length):
#	column = []
#	for seq in aligned_seqs:
#		aa = seq[column_number]
#		if aa != "-":
#			column.append(seq[column_number])
#	uniques = len(set(column))
#	uniques_per_column.append(uniques)
#print (uniques_per_column)
#This for loop goes through "windows" of the uniques per column list and generates a score pased on the (DONT REALLY UNDERSTAND YET)
#window = 10
#numbers_to_plot = []
#for start in range(len(uniques_per_column) - window):
#	win = uniques_per_column[start:start+window]
#	score = sum(win) / len(win)
#	numbers_to_plot.append(score)


#Plotting the conservation:
#plt.figure(figsize=(15,8))
#plt.xlim(0,len(numbers_to_plot)) # Uses the count of the unique amino acid numbers 
#plt.plot(numbers_to_plot,linewidth=3,color="green")
#plt.title('EXERCISE 2')
#plt.ylabel('Unique amino acid residues')
#plt.xlabel('Residue position')
#plt.savefig("Chart_Exercise_2.png",transparent=True)
#plt.show()


