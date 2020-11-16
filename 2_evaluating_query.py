#!/usr/bin/python3

#A piece of code that evaluates the query.txt file to tell the user whether the query yielded good results or if the search should be repeated
import os
os.system("clear")
print ("imported os.\n\n")

#This script is Error trapping the query.txt file. Checks whether any result came back as 0
query_file=open("query.txt").read()


#This for line checks the query file to make sure nothing is 0.
for line in query_file.strip().split("\n"):
	#print (line)
	if line == "0":
		print ("Your query result was 0. That means your query did not yield any results, please try searching again. Maybe try new terms and if you use old ones, please check that they are spelt correctly.")
		exit ()
	else:
		continue 
#print ("Your query has results!")



query_elements=list(query_file.strip().split("\n"))
print("Your search had",query_elements[2],"Results.\n")
#A brief interactive bit to allow the user to choose whether to continue or not

def interact_query (proceed):
		if proceed == "yes" or proceed =="Yes" or proceed =="Y" or proceed =="y":
			print("Fetching protein sequences now, please wait...")
			#IN THIS CASE, RUN BASH SCRIPT THAT DOES EFETCH!
		elif proceed == "no" or proceed =="No" or proceed =="N" or proceed =="n":
			print("You selected no.");
			input ("Press enter or any other key followed by enter to try again...") ;
			os.system("./master_script.sh") ;
			exit()
		else :
			print("Okay, that is not a Yes or a No. We will continue for now, you may review the downloaded seqeunces later and decide from there.")
			interact_query (checkpoint1)
		return print ("\n")
#running the function:
checkpoint1=input("Would you like to fetch the protein files that this search has found? They will be located in the protein_sequences folder. Please answer with yes or no.")	
interact_query(checkpoint1)

