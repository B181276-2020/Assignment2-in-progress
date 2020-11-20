#!/usr/bin/python3
#				Synopsis:
#A script that takes the top 250 alignments from the clustalo alignment output for further processing
import os, sys, shutil
import numpy as np
import matplotlib.pyplot as plt
os.system("clear")
os.chdir("protein_sequences")
alignment= open("seq_alignment_clustalo.msf")

#This finds all sequence headers and puts them into a list
seq_headers = []

counter = 0
for line in alignment:
	counter += 1
	if ">" in line:
		line_fixed=line.replace("\n","")
		seq_headers.append(line_fixed)


#Checks if the file has 250 sequences or more in it
#header_count = len(seq_headers)
#if header_count >= 250:
#	print ("There were more than 250 alignments. It his highly reccomended, #that the amount of sequences are limited to 250.\n\n")



#This section gets all the sequences and puts them into a list. First, splits aligned sequence file at ">" and then prints out only the sequence by finding "]", which marks the end of a sequence and then printing the rest of the list element from that point onwards
counter = 0
seq_only = []
alignment= open("seq_alignment_clustalo.msf").read()
align_list=alignment.replace("\n","").split(">")
for element in align_list:
	starter = element.find("]")
	sequence = element[starter+1:]
	seq_only.append(sequence)
	counter = (counter + 1)

#Now we go through both lists and write them into a file, first a header, then a sequence. stop at 250:

count_to_250 = 0
counter = 0
output_file_250 = open("seq_alignment_250.msf","w")
for headers in seq_headers:
	if counter == 250:
		output_file_250.close()
		break	
	output_file_250.write (seq_headers[counter]+"\n")
	output_file_250.write (seq_only[counter]+"\n\n")
	counter +=1
	
next = input("The 250 best alignment sequences were selected and writen to the file found in protein_sequences/seq_alignment_250.msf. \n Please press enter to continue...")

#This section was used to test if there were indeed 250 aligned sequences in the output file. I left this here for the coding user to check if the code above worked:

#check_file = open("seq_alignment_250.msf").read()
#print (check_file)
#print (len(check_file))
#head_in_out = []
#for line in check_file:
#	counter += 1
#	if ">" in line:
#		head_in_out.append(line)
#print (len(head_in_out))




