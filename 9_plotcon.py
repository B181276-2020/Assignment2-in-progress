#!/usr/bin/python3
#				Synopsis:
#A function for plotconning an input.

#SHOULD ADD AN OPTION FOR THE USER TO USE THESE FUNCTIONS WITH THEIR OWN FASTA FILES IF THEY WISH MAYBE
import os, sys, shutil
os.system("clear")
shutil.copyfile("search.txt", "output_data/search.txt")
os.chdir("output_data")

def plotconthis (alignment,subtitle):
	import os, shutil, subprocess
	print ("Now plotting the conservation of sequences across the protein alignment...")
	#search_info=open("search.txt").read()
	plot="plotcon -sequences "+alignment+" -winsize 12 -graph x11 -scorefile EBLOSUM62 -gsubtitle "+subtitle+" > conservation_plot.png"
	print ("The plot can be found under output_data/conservation_plot.png")
	os.system (str(plot))
	print ("The plot can be found under output_data/conservation_plot.png.\n Press enter to continue...")
	continuing = input("")
	os.chdir("..")
	os.system ("pwd")
	os.system ("python3 0_interface.py")
	return plot
	

#Interactive bit that helps work through 
user_answer = ""
while user_answer not in ("yes", "Yes", "Y*", "no", "No", "N*"):
	user_answer = input("Would you like to plot the conservation of the best 250 alignments? If you select no, all alignments generated will be plotted.(yes/no).")
	if user_answer == ("yes" or "Yes" or "Y*"):
		print("Plotting Conservation of top 250 alignments, please wait...")
		alignment="seq_alignment_250.msf"
		subtitle=open("search.txt").read().replace(" ",",")
		print (subtitle)
		plotconthis(alignment,subtitle)
		print("\n (Your plot can be found under output_data/conservation_plot.png\n")
		os.system("python3 0_interface.py")
		break
	elif user_answer == ("no" or "No" or "N*"):
		print("You selected no.");
		print("Now plotting conservation across all alignments...")
		alignment="seq_alignment_clustalo.msf"
		plotconthis(alignment)
		print("\n (Your plot can be found under output_data/conservation_plot.png\n")
		continuing = input("")
		os.chdir("..")
		os.system("python3 0_interface.py")
		break
	else:
		print("Please answer with yes for \" I want to plot the conservation of 250 alignments \", or no for \"I want to plot all alignments.\"\n")

