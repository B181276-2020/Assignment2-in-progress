#!/usr/bin/bash

#This script acts as the final organisation of the scripts. It will be the only script that has to be run for the whole programme to run.
#First, make the directories needed:


#			Order of Scripts (If ran from top to bottom)

#1. Esearching NCBI for the search terms provided.
python3 1_esearch.py
#Input	: User Input, search terms for taxonomic group and for a protein 
#Process: A wget, that runs an esearch. Processes output to get the query key, 		  number of hits and webenv
#Output	: file containing query key, number of hits and webenv


#2. Evaluating the query to make sure the user is satisfied with the results and doesn't want to repeat the search.
python3 2_evaluating_query.py
#Input	: The query text file
#Process: Evaluating if the query had results and interacting with the user
#Output	: Continue or repeat the process

#3. Efetching the protein sequences that correspond to the query of the user and evaluate the protein sequence
python3 3_efetch.py
#Input	: $key and $webenv 
#Process: An efetch 
#Output	: protein files, into another directory

#4. Allowing the user to choose whether he wants to delete the sequence and try again
python3 4_analyse_or_delete.py
#Input	:
#Process:
#Output	:

#5. Aligning the sequences and generating a plotcon graph
#python3 5_blast_then_plot.py
#Input	:
#Process:
#Output	:

#6. Check if there are more than 250 sequences in the alignment
python3 6_check_if_250.py
#Input	:
#Process:
#Output	:

#7. Extracts the top 250 alignments  ONLY RUNS IF USER CHOOSES TO IN SCRIPT 6
#python3 7_get_top_250.py
#Input	:
#Process:
#Output	:


#8. Analyses the input file using the prosite database and provides a report on all sequences (NOT the top 250)
python3 8_prosite_analysis.py
#Input	:
#Process:
#Output	:

#9. Draws out a graph showing the conservation of amino acids across the aligned top 250 sequences
python3 9_plotcon.py
#Input	:
#Process:
#Output	:





