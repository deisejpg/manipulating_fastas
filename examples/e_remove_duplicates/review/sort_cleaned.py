import os
import sys

input_dir = "/home/brlab/deisejpg/documents/plastome/0_public_matching_ptd/tutorial/output/remove_dup_genes/"
output_dir = "/home/brlab/deisejpg/documents/plastome/0_public_matching_ptd/tutorial/output/sorted/"

#example to run in the command line:
#seqkit sort --quiet -n -i KF156836.rmdupSeq.fasta &> KF156836.rmdupSeq.sorted.fasta
#Note that 'sort' witl fail if any file still has duplicated names

ending = "cln.fa"
new_ending = "cln.sorted.fa"


sort_cln_cmdl = []

for file in os.listdir(input_dir):
    if file[-len(ending):]==ending:
        outfile = file.replace(ending,new_ending)
        sort_cln_cmd = "seqkit sort --quiet -n -i "+input_dir+file+" &> "+output_dir+outfile
    sort_cln_cmdl.append(sort_cln_cmd)

out_run_bash = "./sort_clean_fastas.sh"

with open(out_run_bash, "w") as out:
    for i in sort_cln_cmdl:
        out.write(f'{i}\n')

print("Bash commands to run 'seqkit' to sort the sequences by names are in 'sort_clean_fastas.sh'")
print("Now we run the script in bash.")
run_bash = "bash sort_clean_fastas.sh"
os.system(run_bash)
print("Seqkit run done!")
print("Output files saved at '../output/sorted'.")
