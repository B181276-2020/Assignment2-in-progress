#!/usr/bin/python3

#				Synopsis:
#Script that takes user input: Taxonomic group and Protein family
#Uses input to run an esaearch for these parameters. 
#Use EFetch to generate a query key, webenv code and a integer representing the search mathes. These are then processed and outputted to the file query.txt for later analysis


import os
import shutil
os.system("clear")
print ("imported os and shutil.\n\n")
#saving user input into variables
	#WORKS Hashed for quicker testing
taxo = input("Please provide the taxonomic sub-set you would like to search for. You may search for several taxonomic sub-sets, as long as you connect each extra term with an AND:\n").replace(" ","+")
prot = input("Thank you, now please provide a search term for the type of protein family you want to investigate for. Again, if you would like to search for several protein families, please connect any extra terms you would like to search for with an AND:\n").replace(" ","+")

#Test search terms
#taxo = "Aves"
#prot = "glucose-6-phosphatase"

search=open("search.txt","w")
search.write(taxo)
search.write(" ")
search.write(prot)
search.close()

#print (open("search.txt").read())

#This variables creates my wget 
query=r"""wget -qO- "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=protein&term="""+taxo+r"""*[organism]+"""+prot+r"""*+[protein]+NOT+partial&usehistory=y" """
#print (query)
#This variable saves my awk that gets the WebEnv and query key. Found no easier way to do this.
awk=r""" awk '{
if (FNR==3)
{
split ($0,line,"<|>");
query_key=line[17];
WebEnv=line[21];
hits=line[5];
print query_key > "query_key";
print WebEnv > "WebEnv";
print hits > "hits";
exit ;}}'
"""

#Runs the command
esearch=str(query+"|"+awk)
#print (esearch)
os.system(esearch)

#Assigning the results of the esearch to variables to a text file
query=open("query_key").read()
#print(query)
#print ("did this work")
webenv=open("WebEnv").read()
#print (webenv)
hits=open("hits").read()
#print (hits)


#Writing the output files to query.txt
query_file = open("query.txt","w")
key_file = open("key.txt","w")
webenv_file = open ("webenv.txt","w")

#Writing to query file
query_file.write(query)
query_file.write(webenv)
query_file.write(hits)
query_file.close()

#Writing to key.txt and webenv.txt for later processing 
key_file.write(query)
webenv_file.write(webenv)
key_file.close()
webenv_file.close()
#Checking that the file writing worked
read_query_file =open("query.txt").read()
read_key_file =open("webenv.txt").read()
read_webenv_file =open("key.txt").read()

#print (read_query_file)
#print (read_key_file)
#print (read_webenv_file)


#Housekeeping: removing the files generated by the awk
os.remove("query_key")
os.remove("WebEnv")
os.remove("hits")



