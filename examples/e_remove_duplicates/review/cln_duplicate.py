

import os
import sys

input_dir = "/home/brlab/deisejpg/documents/plastome/0_public_matching_ptd/tutorial/output/fa_files/"
output_dir = "/home/brlab/deisejpg/documents/plastome/0_public_matching_ptd/tutorial/output/remove_dup_genes/"

ending = ".fasta"
new_ending1 = ".cln.fa"
new_ending2 = ".dup.seqs.fasta"
new_ending3 = ".dup.seqs.list"


#example to run in the command line
#seqkit --quiet rmdup -s KF156836.fasta -D KF156836.number_and_list_dupSeqs -d KF156836.dupSeqs &> KF156836.rmdupSeq.fasta
#Note that -s will remove duplicate sequences and -n will remove duplicate names

rmdup_cmdl = []

for file in os.listdir(input_dir):
    if file[-len(ending):]==ending:
        outfile1 = file.replace(ending,new_ending1)
        outfile2 = file.replace(ending,new_ending2)
        outfile3 = file.replace(ending,new_ending3)
        rmdup_cmd = "seqkit --quiet rmdup -n " + input_dir + file+ " -D "+output_dir+outfile3+" -d"+output_dir+outfile2+" &> "+output_dir+outfile1
    rmdup_cmdl.append(rmdup_cmd)


out_run_bash = "./remove_dups.sh"

with open(out_run_bash, "w") as out:
    for i in rmdup_cmdl:
        out.write(f'{i}\n')

print("Bash commands to run 'seqkit' to remove duplicated sequences and genes are in 'remove_dups.sh'")
print("Now we run the script in bash.")
run_bash = "bash remove_dups.sh"
os.system(run_bash)
print("Seqkit run done!")
print("Output files saved at '../output/remove_dup_genes'.")
print("Cleaned files (duplicated sequences and gene names removed) saved with '.cln.fa' ending.")
print("Log files with removed genes saved as fasta or as a list saved with endings '.dup.seqs.fa' and '.dup.seqs.list', respectively.")


#example
#seqkit sort --quiet -n -i KF156836.rmdupSeq.fasta &> KF156836.rmdupSeq.sorted.fasta

#output_dir = "/home/brlab/deisejpg/documents/plastome/0_public_matching_ptd/sorted/"
#new_ending = "cln.sorted.fa"
#for file in os.listdir(output_dir1):
#    if file[-len(ending):]==new_ending1]
#        sort.cmd = "seqkit sort --quiet -n -i " + + new_ending1
