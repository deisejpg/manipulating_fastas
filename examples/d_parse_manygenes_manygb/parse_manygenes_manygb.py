
'''
	In this script we will:

	Extract genes of interest (from a provided list of
	gene names) from multiple GenBank files.

	Note that this will generate files with:
	1. Multiple instances of the same gene if the gene is duplicated in the genome (e.g., rpl2, ycf1, etc.)
	2. Be careful because this script assumes the annotation of the genomes is correct which might not always be true.
	3. Check the number of sequences extracted, visualy inspect the output files
	4. Check scripts downstream to clean up duplicates and poorly annotated regions and to prepare inputs for aligning the sequences

	To run this script use:
	 'python parse_manygenes_manygb.py'
'''

from Bio import SeqIO
import os
from glob import glob
from pathlib import Path

#checking the locations of the files
#change this path if you want to run this script somewhere else
#this is just to get files organized and file names organized
file_directory = '../a_fetch_genbank_files_output/'
file_names = glob('%s/*.gb' % file_directory)

out_dir_path = Path("../d_parse_manygenes_manygb_output/")
if not os.path.exists(out_dir_path):
    os.makedirs(out_dir_path)

print("Reading genbank files from %s" % file_directory)
print("Total number of gb files is: %s" % len(file_names))

#create an object with the path and name of your file with genes of interst to be extracted
gene_list_file = "../b_get_genesOfInterest_list_output/plastome_gene_list.txt"

#define a function that will extract sequences from a gb file based on gene names
def extract_sequence(genbank_file, genes_of_interest):
    #extract gb accession number from the filename to add it to 'Name' qualifier of our SeqIO object later
    #gbaccessionnumberID = os.path.split(genbank_file)[-1]
    gbaccessionnumberID = genbank_file.replace(".gb","")
    gbaccessionnumberID = genbank_file.replace("../a_fetch_genbank_files_output/","")

    #read gb file as a SeqIO class object
    gb_obj = SeqIO.read(genbank_file, 'gb')
    genes = []
    #iterate over the features of the SeqIO object to extract 'gene' information
    for feature in gb_obj.features:
        if feature.type == 'gene':
            genes.append(feature)
    #read the lines of the file with genes of interest
    with open(genes_of_interest, "r") as genel:
        genes_of_interest = [line.strip('\n') for line in genel]
        #iterate over gene names from the gb SeqIO object
        hits = []
        for gene in genes:
            #parse gene names from gb file
            if 'gene' in gene.qualifiers.keys():
               gbf_genename = gene.qualifiers['gene'][0]
               #iterate over gene names of the list of genes of interest
               for i in genes_of_interest:
                  # check when gene names from gb matches genes of interest
                  if gbf_genename in i:
                     #create a SeqIO object and add all the gene names of interest with
                     #their 'Name' as their accession number and keep their sequence
                     extract = gene.extract(gb_obj)
                     extract.id = gbf_genename
                     extract.name = gbaccessionnumberID.replace("../a_fetch_genbank_files_output/","")
                     extract.description = ''
                     #this still returns genes that are duplicated in the plastome such as rpl2 and ycf2
                     #I am going to fix it in when writing a fasta file
                     hits.append(extract)
                     #may try to fix the function later to do it at once
        return(hits)

#test a single file to see if the function is correct
#sequence = extract_sequence("./gb_files/NC_029704.gb", gene_list_file)
#otfile = 'NC_029704.fasta'
#SeqIO.write(sequence,otfile,'fasta')

for file_ in file_names:
    sequence = extract_sequence(file_, gene_list_file)
    otfile = file_.replace('../a_fetch_genbank_files_output/','../d_parse_manygenes_manygb_output/')
    otfile = otfile.replace('.gb','')
    outputfile = '%s.fasta'  % otfile
    print('saving %s' % outputfile)
    SeqIO.write(sequence,outputfile,'fasta')

print("Genes of interest extract for all samples provided in '../d_parse_manygenes_manygb_output/'!")

print("Fasta files saved at '../d_parse_manygenes_manygb_output/'")
