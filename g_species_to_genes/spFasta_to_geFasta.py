'''
	In this script we will:

	Read species fasta files each one of which containing multiple
	 plastome genes
     	Headers are in the format: ">species_name-gene_name"

	To get all the sequences from all the genes for all the species
	 we need to create a nested dictionary.
        The nested dictionary will have the following structure:
        	{Sample_name: {gene_name: sequence}}

     	We will create an empty dictionary "fastas_by_gene" to be our
	 nested dictionary
     	Loop over all the files in the current directory calling
	 fas_to_dict() and storing the data in the dictionary

        To save the files per gene, iterate over the nested dictionary
	 and call dic_to_fas() to create a fasta file for each gene

	Here, dic_to_fas() will create a fasta file for each gene that
	 were store in the nested dictionary and will save it in the
	 current directory

	The structure of the fasta file will be:
	        >sample_name
        	sequence

	 And the name of the file will be:
         	sample_name.fasta
'''

import glob
import os
import sys
from pathlib import Path

def fas_to_dic(fasta_path):
    '''
        Creates a dictionary for each species in which the key is "species_name-gene_name"
        and the value is the sequence of the gene, following the structure:
        {Sample_name: {gene_name: sequence}}
    '''
    fas_out = {}
    with open(fasta_path, "rt") as fasta_in:
        #sp_name = fasta_path.replace(".fa","")
        sp_name = ""
        gene_name = ""
        seq = ""
        for line in fasta_in:
            line = line.strip("\n")
            if not line: continue
            if line.startswith(">"):
                if seq:
                    fas_out[sp_name] = {"gene_name": gene_name,"sequence": seq}
                    seq = ""
                    #print(fas_out[sp_name]) #it looks correct up to here, at least it prints correct
                if len(line.split()) > 1:
                    sp_name = line[1:].split()[0]
                    gene_name = line[1:].split("-")[1:]
                else:
                    sp_name = line[1:].split()[0].strip()
                    gene_name = line.split("-")[-1]
            else:
                seq += line
        if seq:
            fas_out[sp_name] = {"gene_name": gene_name, "sequence": seq}
        return fas_out

def dic_to_fas(in_fasta_dict, out_fasta_path):
     '''
        Takes a dictionary and writes a fasta file
     '''
     opener = open
     if bool(in_fasta_dict):
         with opener(out_fasta_path, "at") as fasta_out:
             for sp_name in in_fasta_dict:
                 if in_fasta_dict[sp_name]['gene_name']:
                     header = f'>{sp_name} {in_fasta_dict[sp_name]["gene_name"]}'.strip()
                     header = f'>{sp_name}'.strip()
                 else:
                     header = f'>{sp_name}'.strip()
                 fasta_out.write(f'{header}\n{in_fasta_dict[sp_name]["sequence"]}\n')
     return out_fasta_path


out_dir_path = Path("../g_species_to_genes_output")
if not out_dir_path.exists():
    out_dir_path.mkdir()

#an empty dictionary to store the data the way we want to save it
fastas_by_gene = {}

#iterating over all the fasta files in the current directory
for file in sorted(list(Path("../e_remove_duplicates_sorted_output").glob("*.fa"))):
    sample_fasta = fas_to_dic(file)
    gene_name = ""
    for seq_name in sample_fasta:
        gene_name = seq_name.split("-")[-1]
        sample_name = seq_name.split("-")[0]
        #adding the data to the dictionary
        if gene_name not in fastas_by_gene:
            fastas_by_gene[gene_name] = {sample_name : 
            {"gene_name":sample_fasta[seq_name]["gene_name"],
            "sequence": sample_fasta[seq_name]["sequence"],}}
        else:
            fastas_by_gene[gene_name][sample_name] = {"gene_name":sample_fasta[seq_name]["gene_name"],
                                                      "sequence": sample_fasta[seq_name]["sequence"]}

#writing one file per genes
for gene in fastas_by_gene:
    #setting up the file name and path
    outfile = Path(out_dir_path, f"{gene}.fa")
    #setting up that I want the genes from the dictionary to be saved in the fasta file
    dic_to_fas(fastas_by_gene[gene], outfile)  
    print(f"The file {outfile} has been created")

#Next we will check the files and prepare the alignment to infer phylogenetic trees
