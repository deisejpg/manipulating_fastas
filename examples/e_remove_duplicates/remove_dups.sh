#fix names of the directories!

#on the command line, before running this script:
#go to the previous output folder to run the for loop (becasue the fasta files are there!
#cd ../d_parse_manygenes_manygb_output
#then, in a single line type (without the '\' at the end of the line):
#for file in *fasta; do echo seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/$file \
# -D ../e_remove_duplicates_output/${file//.fasta/.dup.seqs.list}                             \
# -d ../../e_remove_duplicates_output/${file//.fasta/.dup.seqs.fasta} "&>"                    \
#../../e_remove_duplicates_output/${file//.fasta/.dup.seqs.fasta}

#check if this gives you the correct code (use the lines above or 'seqkip --help' to check the
#flags
#if if looks good, remove 'echo' from the for loop and run it again
#you can add '"&>" remove_dups_local.sh' to the end of the for loop to save the commands on a new file
#cd ../e_remove_duplicates
#mkdir ../e_remove_duplicates_output/
#bash remove_dups_local.sh
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/KF156836.fasta -D ../e_remove_dup_genes_output/KF156836.dup.seqs.list -d ../e_remove_dup_genes_output/KF156836.dup.seqs.fasta &> ../e_remove_dup_genes_output/KF156836.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/KU878156.fasta -D ../e_remove_dup_genes_output/KU878156.dup.seqs.list -d ../e_remove_dup_genes_output/KU878156.dup.seqs.fasta &> ../e_remove_dup_genes_output/KU878156.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/KX904873.fasta -D ../e_remove_dup_genes_output/KX904873.dup.seqs.list -d ../e_remove_dup_genes_output/KX904873.dup.seqs.fasta &> ../e_remove_dup_genes_output/KX904873.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MF359935.fasta -D ../e_remove_dup_genes_output/MF359935.dup.seqs.list -d ../e_remove_dup_genes_output/MF359935.dup.seqs.fasta &> ../e_remove_dup_genes_output/MF359935.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MF359937.fasta -D ../e_remove_dup_genes_output/MF359937.dup.seqs.list -d ../e_remove_dup_genes_output/MF359937.dup.seqs.fasta &> ../e_remove_dup_genes_output/MF359937.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MF359943.fasta -D ../e_remove_dup_genes_output/MF359943.dup.seqs.list -d ../e_remove_dup_genes_output/MF359943.dup.seqs.fasta &> ../e_remove_dup_genes_output/MF359943.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MF359952.fasta -D ../e_remove_dup_genes_output/MF359952.dup.seqs.list -d ../e_remove_dup_genes_output/MF359952.dup.seqs.fasta &> ../e_remove_dup_genes_output/MF359952.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MN078090.fasta -D ../e_remove_dup_genes_output/MN078090.dup.seqs.list -d ../e_remove_dup_genes_output/MN078090.dup.seqs.fasta &> ../e_remove_dup_genes_output/MN078090.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MN711645.fasta -D ../e_remove_dup_genes_output/MN711645.dup.seqs.list -d ../e_remove_dup_genes_output/MN711645.dup.seqs.fasta &> ../e_remove_dup_genes_output/MN711645.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/MZ073672.fasta -D ../e_remove_dup_genes_output/MZ073672.dup.seqs.list -d ../e_remove_dup_genes_output/MZ073672.dup.seqs.fasta &> ../e_remove_dup_genes_output/MZ073672.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_007898.fasta -D ../e_remove_dup_genes_output/NC_007898.dup.seqs.list -d ../e_remove_dup_genes_output/NC_007898.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_007898.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_014697.fasta -D ../e_remove_dup_genes_output/NC_014697.dup.seqs.list -d ../e_remove_dup_genes_output/NC_014697.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_014697.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_019616.fasta -D ../e_remove_dup_genes_output/NC_019616.dup.seqs.list -d ../e_remove_dup_genes_output/NC_019616.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_019616.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_024663.fasta -D ../e_remove_dup_genes_output/NC_024663.dup.seqs.list -d ../e_remove_dup_genes_output/NC_024663.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_024663.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_026690.fasta -D ../e_remove_dup_genes_output/NC_026690.dup.seqs.list -d ../e_remove_dup_genes_output/NC_026690.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_026690.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_026691.fasta -D ../e_remove_dup_genes_output/NC_026691.dup.seqs.list -d ../e_remove_dup_genes_output/NC_026691.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_026691.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_030786.fasta -D ../e_remove_dup_genes_output/NC_030786.dup.seqs.list -d ../e_remove_dup_genes_output/NC_030786.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_030786.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_030789.fasta -D ../e_remove_dup_genes_output/NC_030789.dup.seqs.list -d ../e_remove_dup_genes_output/NC_030789.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_030789.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_031376.fasta -D ../e_remove_dup_genes_output/NC_031376.dup.seqs.list -d ../e_remove_dup_genes_output/NC_031376.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_031376.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_031428.fasta -D ../e_remove_dup_genes_output/NC_031428.dup.seqs.list -d ../e_remove_dup_genes_output/NC_031428.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_031428.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_034914.fasta -D ../e_remove_dup_genes_output/NC_034914.dup.seqs.list -d ../e_remove_dup_genes_output/NC_034914.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_034914.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_035705.fasta -D ../e_remove_dup_genes_output/NC_035705.dup.seqs.list -d ../e_remove_dup_genes_output/NC_035705.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_035705.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_035709.fasta -D ../e_remove_dup_genes_output/NC_035709.dup.seqs.list -d ../e_remove_dup_genes_output/NC_035709.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_035709.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_036052.fasta -D ../e_remove_dup_genes_output/NC_036052.dup.seqs.list -d ../e_remove_dup_genes_output/NC_036052.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_036052.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_036306.fasta -D ../e_remove_dup_genes_output/NC_036306.dup.seqs.list -d ../e_remove_dup_genes_output/NC_036306.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_036306.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_037472.fasta -D ../e_remove_dup_genes_output/NC_037472.dup.seqs.list -d ../e_remove_dup_genes_output/NC_037472.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_037472.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_039973.fasta -D ../e_remove_dup_genes_output/NC_039973.dup.seqs.list -d ../e_remove_dup_genes_output/NC_039973.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_039973.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_041473.fasta -D ../e_remove_dup_genes_output/NC_041473.dup.seqs.list -d ../e_remove_dup_genes_output/NC_041473.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_041473.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_041602.fasta -D ../e_remove_dup_genes_output/NC_041602.dup.seqs.list -d ../e_remove_dup_genes_output/NC_041602.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_041602.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_048520.fasta -D ../e_remove_dup_genes_output/NC_048520.dup.seqs.list -d ../e_remove_dup_genes_output/NC_048520.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_048520.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_053764.fasta -D ../e_remove_dup_genes_output/NC_053764.dup.seqs.list -d ../e_remove_dup_genes_output/NC_053764.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_053764.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_059012.fasta -D ../e_remove_dup_genes_output/NC_059012.dup.seqs.list -d ../e_remove_dup_genes_output/NC_059012.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_059012.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/NC_059942.fasta -D ../e_remove_dup_genes_output/NC_059942.dup.seqs.list -d ../e_remove_dup_genes_output/NC_059942.dup.seqs.fasta &> ../e_remove_dup_genes_output/NC_059942.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/OL450428.fasta -D ../e_remove_dup_genes_output/OL450428.dup.seqs.list -d ../e_remove_dup_genes_output/OL450428.dup.seqs.fasta &> ../e_remove_dup_genes_output/OL450428.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/JQ757046.fasta -D ../e_remove_dup_genes_output/JQ757046.dup.seqs.list -d ../e_remove_dup_genes_output/JQ757046.dup.seqs.fasta &> ../e_remove_dup_genes_output/JQ757046.cln.fa
seqkit --quiet rmdup -n ../d_parse_manygenes_manygb_output/JQ757046.fasta -D ../e_remove_dup_genes_output/JQ757046.dup.seqs.list -d ../e_remove_dup_genes_output/JQ757046.dup.seqs.fasta &> ../e_remove_dup_genes_output/JQ757046.cln.fa
