#!/usr/bin/python3
#				Synopsis:
# A brief script that checks whether there are less than or more than 250 sequences in the alignment file, while interacting with the user

import os, sys, shutil
os.system("clear")
os.chdir("output_data")
alignment= open("seq_alignment_clustalo.msf")
counter = 0

#This makes a list of all the alignment headers
seq_headers = []
for line in alignment:
	counter += 1
	if ">" in line:
		line_fixed=line.replace("\n","")
		seq_headers.append(line_fixed)

#Short section letting the user know that the sequences should be limited
header_count = len(seq_headers)
if header_count > 250:
	print ("There were more than 250 alignments. It his highly reccomended, that the amount of sequences are limited to 250.\n\n")

#Short interactive section letting the user decide to keep the sequences or not
proceed_1 = "check"
while proceed_1 not in ("yes", "Yes", "Y*", "no", "No", "N*"):
	answer = input("Would you like to limit the amount of sequences to 250? If you opt for no, further analysis will be conducted using all sequences(yes/no)\n")
	if answer == ("yes" or "Yes" or "Y*"):
		print("Limiting sequences now. please wait...\n")
		#CONTINUE TO 7_get_top_250_alignments.py
		os.chdir("..")
		os.system("python3 7_get_top_250.py")
		break
	elif answer == ("no" or "No" or "N*"):
		print("You selected no.\n Continuing analysis with all",header_count,"aligned sequences.")
		break
	else:
		print ("Please answer with y for yes, or n for no.\n\n")
