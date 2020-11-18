#!/usr/bin/python3

#YOU DONT NEED PATSEXTRACT! THE FILES ARE ALREADY ON THE SERVER:
os.system("locate posite.dat")

#Just need to patmatmotif:

#patmatmotifs -sequence G6Pase.gb  -outfile first_patmat_result -full -noprune

#NEEDS genbank file:

#esearch -db protein -query "glucose-6-phosphatase [PROT] AND Aves [ORGN]" | efetch -format gb > G6Pase.gb

