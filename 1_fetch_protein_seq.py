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

#Step 1. Use ESearch to find IDs that match an Entrez query and store them on the History server.

#esearch.fcgi?db=protein&term=userinput1[taxonomy]ANDuserinput2[protein]&usehistory=y

echo "Dear user, please provide the taxonomy you would like to search for:"
read taxo
echo "Thank you, now please provide a search term for the protein family:"
read prot

rm -f query.txt
esearch -db protein -query "$taxo AND $prot" | cat > query.txt


#Error trap for bad input, doesnt work yet:
#for line in query.txt
#do
#if [$line = "*>0<*"];
#then
#	echo "No results were found, please run the script again and enter new a new query. \n Please ensure you have spelled all search terms correctly."
#fi
#done < query.txt

#Processing the query.txt file:
while read line ;
do 
replace 





