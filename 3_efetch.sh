#!/usr/bin/bash

#A script that will efetch the authorised query of the user.
key=$(cat key.txt)
echo $key
webenv=$(cat webenv.txt)
echo $webenv
#House keeping:
rm -f query_key
rm -f WebEnv
rm -f hits
rm -f webenv.txt
rm -f key.txt

#Even after house keeping, all the variables retain the value!
echo $key
echo $webenv

#Input: $key and $webenv 
#Process: An efetch 
#Output: protein files, into another directory



