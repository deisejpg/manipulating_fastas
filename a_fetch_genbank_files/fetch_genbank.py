#!/home/brlab/miniconda3/bin/ python

'''
    This script takes one argument, a file with a list of
    accesion numbers (one per line)

    All the accession numbers provided will be downloaded
    from NCBI in genbank format.

    Change "Entrez.email = 'deisejpg@gmail.com'" to your email

    Usage:
    python fetch.gbdata.py accession.names.list.txt

    The format of the file with GenBank accession numbers
    ("accession.names.list.tx"):
    NC_039973
    NC_034914
    NC_053764
    NC_059012
'''

from sys import argv, stdout, exit
import sys
import os
import Bio
from Bio import Entrez
from pathlib import Path

out_dir_path = Path("../a_fetch_genbank_files_output")
if not out_dir_path.exists():
    out_dir_path.mkdir()

#change this to your email!
Entrez.email = 'deisejpg@gmail.com'

#define a function to get an accession number and save it into a file
def fetchGB(searchFor):
    handle = Entrez.efetch(db='nucleotide', id=searchFor, rettype='gb')
    link = searchFor + ".gb"
    local_file = open(link, "w")
    local_file.write(handle.read())
    handle.close()
    local_file.close()

#check if the file with a list of accession numbers is provided as the second argument when running python i.e.:
#python fetch.gbdata.py accession_numbers.txt
if __name__ == '__main__':
    if len(argv) != 2:
        print('Missing file with accession numbers!')
        exit(1)
name = argv[1]

#or comment out the five lines of code above and just read the file:
#name = "./accession.names.list.txt"

'''
   Open the object 'name' to read the file and iterate over each line of the file
   getting each time, one accession number into 'ID' and using that object as the
   argument of fetchGB()
'''
with open(name, 'r') as ins:
    for line in ins:
        ID = line.rstrip('\n')
        print("Getting gb file for ", ID)
        fetchGB(ID)

#then move the '.gb' files to a specific directory 
#this is just to keep the files organized
#comment out if you prefer to keep the files in the current directory
print('Files downloaded!')
print('Files sent to "../a_fetch_genbank_files_output"')
cmd = "mv *.gb ../a_fetch_genbank_files_output"
os.system(cmd)
