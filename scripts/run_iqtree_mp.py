#!/usr/bin/python

'''

	This script takes all alignments in fasta format in the current directory
	and runs IQ-TREE2. Since I have been having trouble with iq2 jobs dying
	without completing the total number of bootstraps intended, I added
	a statement to check if the '.ts.log' files have the number of bootstraps
	I am asking for.

	Usage: python run_iqtree.py DIR fasta_ending number_of_bootstraps
'''

import os
from sys import argv
import glob
from multiprocessing import Process, Pool
import time

def run_iqtree(fasta_file,boots, fasta_name):
    '''Looks for all fasta files in the current directory'''
    time.sleep(0.01)
    cmd = "iqtree2 -nt 3 -st DNA -s "+fasta_file+ " -m GTR+G -b "+boots+" --keep-ident -pre "+fasta_name+"ts"
    print(cmd)
    return os.system(cmd)

def check_iq_finished(DIR, aln_end):
    '''Checks if the iqtree job has finished'''
    for file in os.listdir(DIR):
        if file.endswith(aln_end):
            fasta_name = file.replace(aln_end,'')
            with open("./"+fasta_name+"ts.log", "rt") as log:
                last_line = log.readlines()[-1]
                #print(last_line)
                if last_line.startswith("Date and Time:"):
                    print()
                    print(f"{fasta_name} complete successfully: {last_line}")
                elif len(fasta_name+"ts.boottrees") != 100:
                    print(f"Flagged an incomplete run for {file}. Restarting {file} run.")
                    time.sleep(0.01)
                    cmd = "iqtree2 -nt AUTO -redo -st DNA -s "+file+ " -m GTR+G -b "+boot+" --keep-ident -pre "+fasta_name+"ts"
                    print(cmd)
                    return os.system(cmd)


'''checking if the user provided all the arguments to run the script '''
if __name__ == "__main__":
    if len(argv) !=4:
        print("It seems that you forgot something!")
        print("Usage:   python run_iqtree.py bootstrapInt")
        print("Example: python run_iqtree.py 10")
        exit(1)
    DIR = argv[1]
    aln_end = argv[2]
    boot = argv[3]

    pool = Pool(processes=4)
    results = []

    for file in os.listdir(DIR):
        if file.endswith(aln_end):
            #for ffile in range(1,len(file)):
            fasta_name = file.replace("aln-cln", '')
            #print(fasta_name)
            results.append(pool.apply_async(run_iqtree, (file,boot,fasta_name)))
    print([result.get() for result in results])
    #print(results)
    #print(pool.map(run_iqtree, (file,str(boot),fasta_name), [file for i in range(1,78)]))

    processes = []
    for i in os.listdir(DIR):
        if file.endswith(aln_end):
            fasta_name = file.replace("aln-cln", '')
            processes.append(Process(target=run_iqtree, args=(file,boot,fasta_name)))

    #for file in os.listdir(DIR):
    #    if file.endswith(aln_end):
    #        fasta_name = file.replace(aln_end, '')
    #        p = Process(target=run_iqtree, args=(file,boot, fasta_name, lock))
    #        print(p)
    #        p.start()
    #        p.join()
            #check_iq_finished(DIR, aln_end)
    #print("All processes have completed!")

print()
print("It seems that all files have been completed successfully!")
print()

check_iq_finished(DIR, aln_end)
