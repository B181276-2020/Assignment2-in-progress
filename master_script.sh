#!/usr/bin/bash

#This script acts as the final organisation of the scripts. It will be the only script that has to be run for the whole programme to run.
#First, make the directories needed:

#1. This directory will contain the protein sequences desired by the user:
	#Hashed to stop renewing directory
#mkdir protein_sequences
#ls
#

###################Order of Scripts##################
#1. Esearching NCBI for the search terms provided.
./1_esearch.py

#2. Evaluating the query to make sure the user is satisfied with the results and doesn't want to repeat the search.
python3 2_evaluating_query.py

#3. Efetching the protein sequences that correspond to the query of the user and evaluate the protein sequence
./3_efetch.sh

#4. Allowing the user to choose whether he wants to delete the sequence and try again
./4_analyse_or_delete.sh




