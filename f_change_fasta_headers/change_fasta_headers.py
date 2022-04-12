
'''
	It takes a fasta file with headers like ">gene_name"
	and change them to add the name of the file (which is
	the species name) to the beginning of the header,
	to look like this: ">Sample_name-gene_name

	Usage:
	python fix_fasta_headers.py
'''

import sys, os

if __name__ == "__main__":
	DIR = "../e_remove_duplicates_sorted_output/"


for sp_file in os.listdir(DIR):
    if sp_file.endswith(".fa"):
        sp_name = sp_file.replace(".cln.sorted.fa", "")
        infile = open("../e_remove_duplicates_sorted_output/"+sp_file)
        outfile = open("../f_change_fasta_headers_output/" + sp_name + ".fa", "w")
        for line in infile:
            if line.startswith(">"):
                line = line.replace(">","").strip("\n")
                if not line.startswith(sp_name):
                    new_header = ''
                    new_header += ">" + sp_name + "-" + line
                outfile.write(new_header + "\n")
            else:
                outfile.write(line)
        print(sp_name+ "'s headers are renamed!")
        print("Files saved as '.fa' at '../f_change_fasta_headers_output'")

