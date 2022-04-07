
'''
	In this script we will:

	Extract sequences of multiple genes from a single GenBank file.

 	Skip this step if you want to extract sequences of multiple genes
	 from multiple GenBank files.

	Each file generated will have one sequence per gene. In this case,
	 77 plastid protein-coding genes. 

	To run this script:
	 'python parse_manygenes_singlegb.py'

	Note that you may have to change the paths of 'plastome_gene_list.txt'
	 and the path to the genbank file below.

	You can also change the path to where the fasta file will be written.
'''

from Bio import SeqIO
import os
from glob import glob
from pathlib import Path

#we generated a file with genes of interest in the previous step
gene_list_file = "../b_get_genesOfInterest_list_output/plastome_gene_list.txt"

with open(gene_list_file, "r") as genel:
    gene_names=[line.strip('\n') for line in genel]
#check if we are getting the number of genes we are expecting
#print(len(gene_names))

#reading and preparing the gb file
gbfile = "../a_fetch_genbank_files_output/KF156836.gb"
gb_object = SeqIO.read(gbfile, "gb")
allgenes=[feature for feature in gb_object.features if feature.type == 'gene']
#print(len(allgenes))

#create an empty list to append the information we will extract from the gb file
gene_sequences = []

for gene in allgenes:
    if 'gene' in gene.qualifiers.keys():
        geneName=gene.qualifiers['gene'][0]
        if geneName in gene_names:
            extract=gene.extract(gb_object)
            extract.id=geneName
            extract.description=''
            gene_sequences.append(extract)
            print('gene %s has been found' % geneName)

out_dir_path = Path("../c_parse_manygenes_from_singlegb_output")
if not out_dir_path.exists():
    out_dir_path.mkdir()

#create an object to write the outpur file
outfile_fasta = '../c_parse_manygenes_from_singlegb_output/KF156836_ptdgenes.fa'

#use the attribute write of SeqIO to write a fasta file with genes and respective sequences of interest
SeqIO.write(gene_sequences, outfile_fasta, 'fasta')

print("Genes of interest of accession 'KF156836' saved at '../c_parse_manygenes_from_singlegb_output/' as 'KF156836_ptdgenes.fa'")
