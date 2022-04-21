
'''
	In this script we will:

	1. Read a genbank file and extract only genes of interest.
	In this case, I am excluding orfs, tRNAs, and rRNAs.
	I am selecting only protein-coding genes of the chloroplast
	genome (plastome).

	This script will produce a list of genes that will be saved
	with one gene per line in a file in the current directory.

	Note that I am not including the gene rps12 (a protein-coding
	gene) because it is a transpliced gene and due to its variation
	in the order that I am studying (Ericales; sometimes it is not
	transpliced), I opted not to add the gene in downstream analyses.

	To run this script, type:
	'python get_genesOfInterest_list.py'
'''

from Bio import SeqIO
import os
from glob import glob
from pathlib import Path

#use one file that has all the genes of interest
gbfile = "../a_fetch_genbank_file_output/KF156836.gb"

record = SeqIO.parse(gbfile, "genbank")
rec = next(record)

gene_list_clean = []
gene_name = []
gene_loc = []

for f in rec.features:
    if f.type == 'gene':
        gene_name = f.qualifiers['gene']
        gene_loc = f'gene_location {f.location}'
        gene_list = []
        for gene in gene_name:
            if gene.startswith("trn") or gene.startswith("inf") or gene.startswith("rrn") or gene.startswith("ycf15") or gene.startswith("orf") or gene.startswith("rps12"):
                continue
            else:
                gene_list.append(gene)
                [gene_list_clean.append(x) for x in gene_list if x not in gene_list_clean]

#checking what I have in gene_list_clean
#should be 77 plastid protein-coding genes for this project
#print(str(gene_list_clean))
#print(len(gene_list_clean))


#save the list of genes of interest without repetition
out_dir_path = Path("../b_get_genesOfInterest_list_output/")
if not out_dir_path.exists():
    out_dir_path.mkdir()

outfile = f'plastome_gene_list.txt'
with open(outfile, "w") as outf:
    for i in gene_list_clean:
        outf.write(f'{i}\n')

print("List of genes of interest saved at '../b_get_genesOfInterest_list_output/plastome_gene_list.txt'")
cmd = "mv *.txt ../b_get_genesOfInterest_list_output/"
os.system(cmd)

#Next we can either parse genes from one genbank file in step "c"
#Or we can go to step "d" and parse genes from multiple gb files
