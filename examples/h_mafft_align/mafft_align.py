'''
	This script takes unaligned fasta files and
        runs mafft for all the files ending with "fasta"
        in the current directory.

        Aligned files are saved with "aln.fas" endings.

	Mafft needs to be on the path for you to run it
	using "mafft." If it is not on your path, provide
	the absolute path to the software.

        Usage:
	python mafft_align.py

'''
import os

for infile in os.listdir("./"):
    if infile.endswith(".fasta"):
        outfile = infile.replace("fasta","aln.fas")
        process = f'mafft --thread 6 --auto {infile} >> {outfile}'
        os.system(process)
