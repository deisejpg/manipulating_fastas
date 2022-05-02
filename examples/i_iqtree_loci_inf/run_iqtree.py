#!/usr/bin/python

'''

        This script takes all alignments in fasta format in a given directory
        and runs IQ-TREE2. Since I have been having trouble with iq2 jobs dying
        without completing the total number of bootstraps intended, I added
        a statement to check if the '.ts.boottrees' files have the number of
        bootstraps I am asking for.
        Usage: python run_iqtree.py bootstrapInt

	*This runs one job at a time*
'''

import os
from sys import argv

''' checking if the user provided all the arguments to run the script '''
if __name__ == "__main__":
    if len(argv) !=2:
        print("It seems that you forgot something!")
        print("Usage:   python run_iqtree.py bootstrapInt")
        print("Example: python run_iqtree.py 100")
        exit(1)
    boot = argv[1]

'''Looks for all fasta files in the current directory'''
for fasta_file in os.listdir("./"):
    ''' considers only files that end with '.aln-cln'''
    if fasta_file.endswith(".aln-cln"):
        ''' fasta_name is the name of the gene, which is the name of the file without the ending'''
        fasta_name = fasta_file.replace(".aln-cln", "")
        '''checks if main output file of iqtree was created
           and if not, it runs iqtree '''
        if not os.path.exists("./"+fasta_name+".ts.treefile"):
            cmd = "iqtree2 -nt AUTO -st DNA -s "+fasta_file+ " -m GTR+G -b "+boot+" --keep-ident -pre "+fasta_name+".ts"
            print(cmd)
            os.system(cmd)
            ''' if there is an output file for iqtree, checks if '.boottrees'
                has all the expected bootstraps'''
        elif len(fasta_name+".ts.boottrees") != 100:
            print(f"Flagged incomplete run for {fasta_file}. Restarting {fasta_file} run.")
            cmd = "iqtree2 -nt AUTO -st DNA -s "+fasta_file+ " -m GTR+G -b "+boot+" --keep-ident -pre "+fasta_name+".ts"
            print(cmd)
            os.system(cmd)
        else:
            print(f"{fasta_file} completed successfully")
print()
print("All files completed successfully!")
