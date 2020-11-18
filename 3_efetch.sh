#!/usr/bin/bash

#A script that will efetch the authorised query of the user.
key=$(cat key.txt)
webenv=$(cat webenv.txt)
echo -e "Processing the following key and web enviornment:\n" "Key:" $key "\n Web enviornment:" $webenv "\n\n"

#Trying something else:


#Input: $key and $webenv 
#Process: An efetch 
#Output: protein files, into another directory

#fasta version:
#WORKS hashed so that download doesn't happen again
#wget -O proteinseq.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key=$key&WebEnv=$webenv&rettype=fasta&retmode=text"

#Genbank version: DOESNT WORK, FIX THIS
#wget -O proteinseq_genbank.gb "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key=$key&WebEnv=$webenv&rettype=genbank&retmode=text"

#A case version of a while statement, checking whether the user wants to continue or not. THIS WORKS IM SO PROUD

while true; do
    read -p "Do you want to print the protein sequences to the screen?(y/n)" yn
    case $yn in
        [Yy] ) echo "You said yes! Here are the protein sequences"; cat proteinseq.fasta ; echo "These are the protein seqeunces downloaded.";;
        [Nn] ) echo -e "Okay, if you would like to see your protein seqeunces, they can be found in the directory \"protein_seqeunces/proteinseq.fasta\".";exit;;
        * ) echo "Please answer y for yes or n for no.";;
    esac
done


#House keeping: Hashed for now

rm -f webenv.txt
rm -f key.txt
rm -f query.txt
#Even after house keeping, all the variables retain the value!
