#!/usr/bin/python3
import os, shutil
os.system("clear")
#				Synopsis:
# A function that splits up a genbank file and saves it to a list. It then runs a for loop on each element and generates a patmatmotif file. The patmatmotif file gets opened and its contents saved to a output file.

#YOU DONT NEED PATSEXTRACT! THE FILES ARE ALREADY ON THE SERVER:
os.system("locate posite.dat")
shutil.copy("proteinseq_genbank.gb", "protein_sequences/proteinseq_genbank.gb")
os.chdir ("protein_sequences")
#Just need to patmatmotif:
print ("Now processing the motifs found in all the sequences. Please press enter to continue...")
#HASHED FOR NOW
input("")


#Function writing the result of the patmats to a single file
def patmatallsequences (genbank_file):
	infile = open(genbank_file).read()
	#print (infile)
	#Have to account for special individuals who use the spilting convetion in their genbank file
	genbanks = infile.replace("//w","$$$$$")
	each_genbank = genbanks.split("//")
	n_genfiles = len(each_genbank)
	print (n_genfiles)
	input("")
	#This accounts for if the output file already exists
	
	if os.path.exists ("motifs_in_sequences.out"):
		os.remove ("motifs_in_sequences.out")
	
	count = 0
#This generates a patmatmotif analysis for each file and outputs the results to the file "motifs_in_sequences.out
	for element in each_genbank:
		#This stops the code from dying when there are no more gen files 			  to process
		print ("Scanning sequences against PROSITE database, please wait...")
		count += 1
		if count == n_genfiles:
			print ("TRIGGERED BREAKER")
			break
		else:
			print ("This is the count:", count)
			print ("This is the number of files:", n_genfiles)
			os.system("touch patmat_infile.gb")
			patmat_infile = open("patmat_infile.gb","w")
			patmat_infile.write(element)
			patmat_infile.close()
			os.system("patmatmotifs -sequence patmat_infile.gb -outfile motifs_temp.out -full -noprune -auto -die")
			motif_file = open("motifs_temp.out").read()
			output_file = open("motifs_in_sequences.out","w")
			output_file.write(motif_file)
			output_file.close()
			os.remove ("motifs_temp.out")
			os.remove ("patmat_infile.gb")

temp_input = "proteinseq_genbank.gb"
patmatallsequences(temp_input)

#Fixing the "accounting for lack of consistency in splitting convention"
motifs = open("motifs_in_sequences.out").read()
motifs_fixed = motifs.replace("$$$$$","//w")
motifs_fixed.close()
os.remove("motifs_in_sequences.out")
motifs = open("motifs_in_sequences.out","w")
motifs.write(motifs_fixed)
motifs.close()

#check if it worked
motifs = open("motifs_in_sequences.out").read()
print (motifs)

print ("This is the analysis of all the protein motifs that could be found in the sequences, when scanned against the Prosite database. \n It can be found under protein_sequences/motifs_in_sequences.out")


#NOT DONE YET!!!!!!!!!!!!!!!!!!!!!!!!
#NEEDS genbank file:

#esearch -db protein -query "glucose-6-phosphatase [PROT] AND Aves [ORGN]" | efetch -format gb > G6Pase.gb

