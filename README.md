# Manipulating fasta files for phylogenetic analysis

__./scripts/__ directory has all the scripts used in the 'examples' pipeline

__./examples/__ directory has the example of a pipeline to go from downloading 
files from genbank, to preparing alignments and inferring phylogenies

Find below some thorough explanation on how to use the 'examples' pipeline:

This is intended to teach students step by step some ways to manipulate fasta 
files. The organization in multiple directories is solely to keep it simple 
for for students to visualize what is input and what it output. Even if you 
are not used to it, read through the scrips as I provide documentation on 
what is being done in each step. Send me an email if you have any questions!

In `a_fetch_genbank_files`, the user can download selected accession numbers 
fro genbank provided in a separate file with one accession number per line. 
After running this script, you files will be saved in 
`a_fetch_genbank_files_output`. As a way to practice, try to change the code
to save the files in the current directory. 
*Tip: check the last four lines of code!*

In `b_get_genesOfInterest_list`, one can select genes of interest from one 
of the genomes that were downloaded in the previous step. The output file will
be in `b_get_genesOfInterest_list_output`. If you already have a list of of 
gene names that you are interested in, go to the next step, 
`c_parse_manygenes_from_singlegb`. Keep in mind that is always good to 
visualize your data and to confirm annotations of data downloaded from public 
databases.

The next two directories have scripts to parse the data from genbank files. 
If you want like to parse genes from a single file, go to 'c'. If you want 
to parse multiple genes from multiple files at the same time, go to `d_parse_manygenes_manygb`.
'c' and 'd' will output fasta files in the following format:
    - one fasta file per species
    - fasta header ">gene_name"

In `e_remove_duplicates`, we remove duplicate sequences. This is a step that
may give you trouble if there were problems in the annotations of the genomes. 
However, it is normal to find duplicated genes in a genome and if we want to 
keep a single copy, we have to remove the ones that are repeated and keep only 
unique sequences. For this step, I started python scripts that are currently 
in the subdirectory 'review', but ended up running a for loop in the command 
line and generating a simple bash script to run seqkit (a command line tool) 
to remove duplicated sequence names and a second one to sort. As soon as I 
have time I will finish reviewing the python scripts to do both steps at once,
but I think it is also important to be practical and I find it 
quicker to run a single for loop to generate the commands to all files. Check
the first few lines of the bash scripts for the for loops.

In `f_change_fasta_headers`, the script takes a fasta file with headers named as 
'>gene_name' and changes the headers to ">Sample_name-gene_name", considering that
"Sample_name" is the name of the file. Depending on the analyses you are running, 
it is good to have both the species and the gene names in the header. For example,
if you want to align genes from different species you need to shuffle species of 
each gene in fasta files for each. That's our next step.

In `g_species_to_genes`, first we use __checking.sh__ that all our fasta files have
the number of genes we expect. They don't necessarily have to have the same number 
because the gene may have been lost in some species, or the record on the public
database was incomplete. In any case it is important to check and it is also 
pretty quick and simple.
Next, the script __spFasta_to_geFasta.py__ reads fasta files that are organized by
species, with all the genes for that given species and with headers like 
">species_name-gene_name". This script outputs are fasta files per gene with
headers like ">sample_name." Read the script description for more details. This is
a great resource to practice python dictionaries!


<p align="center">
  <img 
    src="/images/Pipeline_diagram_2.jpg"
  >
</p>


Next, I will add scripts to align the data and to infer and manipulate phylogenies.


__Happy coding!__

*To do:*
Fix names of the directories and python bash/scripts in e_remove_duplicates
