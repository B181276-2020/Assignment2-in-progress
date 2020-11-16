#!/usr/bin/bash
#Writen 09/11/2020 
#				Synopsis:
#Script that takes user input: Taxonomic group and Protein family
#Uses input to run an esaearch for these parameters. 
#Results are
#Use EPOST to store the UIDs on the history server, outputs a query key and Weeb enviornment
#Use EFetch to take the list of UIDs and downloads them. 

# 1. Esearch:
# Example query structure: human[organism] AND topoisomerase[protein name]
# No operators are required if UIDs are searched

#Step 1. Use ESearch to find IDs that match an Entrez query and store them in a file

#esearch.fcgi?db=protein&term=userinput1[taxonomy]ANDuserinput2[protein]&usehistory=y

#This part asks the user to provide a taxonomic group and a protein search term. 

#Works, hashed out to make testing faster
#echo "Dear user, please provide the taxonomic sub-set you would like to search for:"
#read taxo
#echo "Thank you, now please provide a search term for the type of protein you want to investigate for:"
#read prot

#Replacing spaces with a plus so that the esearch works!

#Test search terms
	#Good test
rm -f search.txt
echo $taxo $prot > search.txt
taxo="Aves"
prot="glucose-6-phosphatase"
prot=${prot/ /+}
#prot= echo $prot"[prot]"
#echo $prot
taxo=${taxo/ /+}
	#Bad test
#taxo="suck44333it209rurhefnoi2r1"
#prot="why1ßrjßp23mnfpi3nrp1"

#THIS IS SO MUCH EASIER: good for test
#esearch -db protein -query "$taxo+$prot" | efetch -format fasta > proteinseq.fasta
#more proteinseq.fasta

echo -e "Now searching the NCBI protein database for the protein relating terms:" $prot "\nIn the taxonomic group:" $taxo
rm -f query.txt
#An automated version of the esearch to plus extracting the query key and webenv using awk.
wget -qO- "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=protein&term=$taxo[organism]+$prot+[protein]&usehistory=y" | awk '{
if (FNR==3)
{
split ($0,xml_line_split,"<|>");
query_key=xml_line_split[17];
WebEnv=xml_line_split[21];
hits=xml_line_split[5];
print query_key > "query_key";
print WebEnv > "WebEnv";
print hits > "hits";
exit ;}}'
#Reads each line, make conditional so that it only works on the third line


#House keeping:
rm -f query.txt

#Assigning the results of the esearch to variables to a text file
query_key=$(cat query_key)
echo $query_key >> query.txt
echo $query_key >key.txt
WebEnv=$(cat WebEnv)
echo $WebEnv >> query.txt
echo $WebEnv >webenv.txt
hits=$(cat hits)
echo $hits >> query.txt

cat query.txt

#House keeping:
rm -f query_key
rm -f WebEnv
rm -f hits









