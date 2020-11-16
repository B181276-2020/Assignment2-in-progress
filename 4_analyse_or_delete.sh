#!/usr/bin/bash

#A short case version of a while statement to allow the user to delete the proteinseq.fasta file and interrupt the program. Re-runs the whole program if the user chooses to delete the file.
while true; do
    read -p "Would you like the programme to analyse this sequence or delete the download?(y for analyse/n for delete)" yn
    case $yn in
        [Yy]* ) echo "Now continuing to analysis...";exit;;
        [Nn]* ) echo -e "Deleting results of esearch now. Now re-running the search section of the program. Press enter to continue...";rm -f proteinseq.fasta;read enter;./master_script.sh;exit;;
        * ) echo "Please answer with y for analyse or n for delete.";;
    esac
done
