'''

        This script takes fasta files with sequences in multiple lines
        and saves new files with sequences in a single line.

        The script will go through all the files that end in "FNA"
        in the current directory and will save new files ending in "fasta"

        To run this script you need to have seqkit installed on your 
        computer. If you don't want to install it, check "linearizeFasta.py." 

        Usage:
        python linearizeFasta_seqKit.py
'''

import os
import sys

#looping over all files in the current directory
for infile in os.listdir("./"):
    #considering only the files that end with "FNA"
    if infile.endswith(".FNA"):
        #shell command to linearize the sequences of the fasta file
        #saving into a new file
        cmd = f"seqkit seq -w 0 {infile} >> {infile.replace('.FNA','.fasta')}"
        os.system(cmd)
