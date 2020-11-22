#!/usr/bin/bash

#This script acts as the final organisation of the scripts. It will be the only script that has to be run for the whole programme to run.
#First, make the directories needed:


#			Order of Scripts (If ran from top to bottom)

#1. Esearching NCBI for the search terms provided.
python3 1_esearch.py
#Input	: User Input, search terms for taxonomic group and for a protein 
#Process: A wget, that runs an esearch. Processes output to get the query key, number of hits and webenv
#Output	: file containing query key, number of hits and webenv


#2. Evaluating the query to make sure the user is satisfied with the results and doesn't want to repeat the search.
python3 2_evaluating_query.py
#Input	: The query text file
#Process: Evaluating if the query had results and interacting with the user
#Output	: Continue or repeat the process

#3. Efetching the protein sequences that correspond to the query of the user and evaluate the protein sequence
python3 3_efetch.py
#Input	: the contents of the query.txt file
#Process: An efetch 
#Output	: files containing the alignment sequences, one fasta: proteinseq

#4. Allowing the user to choose whether he wants to delete the sequence and try again, or continue to analysis. Just a short decision tree
python3 4_analyse_or_delete.py
#Input	: User input, asking if they want to continue or not
#Process: Processes user input, evaluating it
#Output	: Either deletes the generated files and takes the user to the user interface or continues to analysis

#5. Aligns the sequences generated from the efetch 
python3 5_aligner.py
#Input	: The input file is the fasta file generated in script 3
#Process: Generates a string that acts as a clustalo command and then system calls it
#Output	: A .msf file detailing the alignments called 

#6. Check if there are more than 250 sequences in the alignment
python3 6_check_if_250.py
#Input	: The aligned sequences generated from script 5
#Process: Checks if the number of sequences exceeds 250. If so, script 7 is run, which trims it down and outputs a new file
#Output	: Either runs script 7 or leaves the files alone and continues

#7. Extracts the top 250 alignments  ONLY RUNS IF USER CHOOSES TO IN SCRIPT 6
#python3 7_get_top_250.py
#Input	: An alignment file exceeding 250 sequences
#Process: Trims the best 250 sequences off of the file
#Output	: A file containing the 250 best alignments called seq_alignment_250.msf


#8. Analyses the input file using the prosite database and provides a report on all sequences (NOT the top 250)
python3 8_prosite_analysis.py
#Input	: The  file proteinseq_genbank.gb (was writen as a function, so it can be used independently, option in user interface)
#Process: Goes through the genbank file and takes each protein sequence, finds the motifs and writes them to the file motifs_in_sequences.out
#Output	: The file motifs_in_sequences.out

#9. Draws out a graph showing the conservation of amino acids across the aligned top 250 sequences
python3 9_plotcon.py
#Input	: The seq_alignment_250.msf file containing the best 250 alignments (was writen as a function, so it can be used independently, option in user interface)
#Process: Generates a plotcon command and then runs a plotcon. It creates a plot of the conservation across the sequence alignments
#Output	: A plotcon conservation alignment graph, saved as user_plot.png





