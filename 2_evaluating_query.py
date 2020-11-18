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
print ("Your query has results!")



query_elements=list(query_file.strip().split("\n"))
print("Your search had",query_elements[2],"Results.\n")

#Checking that the query is not too long
too_long = ""
if int(query_elements[2]) > int(1000):
	print ("Your query has more than 1000 results. This means that analysis could be slow.\n")
	too_long=input("If you would like to continue press enter. If you would like to repeat the search, please type any character followed by enter to enter a new search.")
#This if statement restarts the whole programm if the search was too long
if too_long != "":
	print ("restarting search now...\n Press enter to continue.")
	input()
	os.system("./master_script.sh")
	exit()


#A interactive loop that asks the user if they want to continue to fetch the protein sequence
proceed_1 = "check"
while proceed_1 not in ("yes", "Yes", "Y*", "no", "No", "N*"):
	answer = input("Would you like to fetch the protein files that this search has found? They will be located in the protein_sequences folder (yes/no).")
	if answer == ("yes" or "Yes" or "Y*"):
		print("Fetching protein sequences now, please wait...")
		break
	elif answer == ("no" or "No" or "N*"):
		print("You selected no.");
		input("Press enter or any other key followed by enter to enter a new search...") ;
		os.system("./master_script.sh") ;
		print ("Would execute master script again here")
		exit()
	else:
		print ("Please answer with y for yes, or n for no.\n\n")




