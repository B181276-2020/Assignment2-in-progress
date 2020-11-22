#!/usr/bin/python3
#				Synopsis:
#A script that will efetch the authorised query of the user.
import os,shutil
os.system("clear")
print("imported os and shutil.")
key = open("key.txt").read().strip("\n")
webenv = open("webenv.txt").read().strip("\n")

print ("Your esearch results yielded the following query key and web enviornment:\nKey: "+key+"\nWeb enviornment:"+webenv+"\n\n")

#Function for running the efetch
def downloadseq (query,web_env):
	#Creates two strings, using the input for query and webenv, to make a 		 system call to run the bash wget command
	fasta_call = "wget -O proteinseq.fasta \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key="+query+"&WebEnv="+web_env+"&rettype=fasta&retmode=text\""
	print (fasta_call)
	genbank_call = "wget -O proteinseq_genbank.gb \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key="+query+"&WebEnv="+web_env+"&rettype=gb&retmode=text\""
	os.system(fasta_call)
	os.system(genbank_call)
	print ("\n\nThe protein sequences were downloaded! Two versions of the files exist, one in fasta format, the other in genbank format. The files can be found under output_data/proteinseq.fasta and output_data/proteinseq_genbank.gb respectively")
	shutil.copy("proteinseq.fasta", "output_data/proteinseq.fasta")
	shutil.copy("proteinseq.fasta", "output_data/proteinseq_genbank.gb")
	return fasta_call,genbank_call

#Running the function: (hashed for now)
downloadseq (key,webenv)

#House keeping: (hashed for now)
os.remove("webenv.txt")
os.remove("key.txt")
os.remove("query.txt")

#Interactive bit that lets the user output the protein sequence to the screen if they want and also takes them back to the home screen if they choose to.


proceed = "check"
proceed_2 = "check"
while proceed not in ("yes", "Yes", "Y", "y" "no", "No", "N"):
	answer = input("Would you like to print the protein sequences to the screen? (yes/no)")
	if answer == ("yes" or "Yes" or "Y" or "y"):
		fasta = open("proteinseq.fasta").read()
		print (fasta)
	elif answer == ("no" or "No" or "N" or "n"):
		print("You selected no.\n")
		print("if you would like to see your protein seqeunces, they can be found in the directory \"output_data/proteinseq.fasta\".\n")
		while proceed_2 not in ("yes", "Yes", "Y*", "no", "No", "N*"):
			answer_2 = input("Would you like to continue to assessing the sequences for alignment? If you select no you will be taken back to the user interface.(yes/no)")
			if answer_2 == ("yes" or "Yes" or "Y*"):
				proceed = "yes"
				break
			elif answer_2 == ("no" or "No" or "N*"):
				proceed = "no"
				os.system("python3 0_interface.py")
			else:
				print ("Please answer with y for yes, or n for no.\n\n")
	else:
		print ("Please answer with y for yes, or n for no.\n\n")






# THIS WHOLE SECTION WAS PREVIOUSLY IN BASH, KEPT IT IN INCASE A CODER WANTS TO USE BASH CODE
#INSERT SHEBANG FOR BASH HERE

#				Synopsis:
#A script that will efetch the authorised query of the user.


#key=$(cat key.txt)
#webenv=$(cat webenv.txt)
#echo -e "Processing the following key and web enviornment:\n" "Key:" $key "\n Web enviornment:" $webenv "\n\n"

#Trying something else:


#Input: $key and $webenv 
#Process: An efetch 
#Output: protein files, into another directory

#fasta version:
#WORKS hashed so that download doesn't happen again
#wget -O proteinseq.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key=$key&WebEnv=$webenv&rettype=fasta&retmode=text"

#Genbank version: DOESNT WORK, FIX THIS
#wget -O proteinseq_genbank.gb "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&query_key=$key&WebEnv=$webenv&rettype=gb&retmode=text"

#A case version of a while statement, checking whether the user wants to continue or not. THIS WORKS IM SO PROUD

#while true; do
#    read -p "Do you want to print the protein sequences to the screen?(yes/no)" yn
#    case $yn in
#        [Yy] ) echo "You said yes! Here are the protein sequences"; cat #proteinseq.fasta ; echo "These are the protein seqeunces downloaded.";;
#        [Nn] ) echo -e "Okay, if you would like to see your protein seqeunces, they can be found in the directory \"output_data/proteinseq.fasta\".";exit;;
#        * ) echo "Please answer y for yes or n for no.";;
#    esac
#done


#House keeping: Hashed for now

#rm -f webenv.txt
#rm -f key.txt
#rm -f query.txt
#Even after house keeping, all the variables retain the value!
