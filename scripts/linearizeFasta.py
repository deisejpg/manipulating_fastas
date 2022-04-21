'''

	This script takes fasta files with sequences in multiple lines
	and saves new files with sequences in a single, very long line.

	The script will for through all the files that end in "FNA"
	in the current directory and will save new files ending in "fasta"

	Usage:
	python linearizeFasta.py
'''

import os
import sys
from Bio import SeqIO

#looping over all files in the current directory
for infile in os.listdir("./"):
    #considering only the files that end with "FNA"
    if infile.endswith(".FNA"):
        #open "FNA" files
        with open(infile) as fasta:
            #placeholder for the output file with "fasta" ending
            outfile = open(infile.replace("FNA","fasta"), "w")
            #list comprehension to linearize the sequences of the fasta file 
            #saving into a new file
            [outfile.write(f">{r.id}\n{r.seq}\n") for r in SeqIO.parse(fasta, "fasta")]
