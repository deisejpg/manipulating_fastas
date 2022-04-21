#!/bin/bash

for file in *fasta
do
    mafft --thread 6 --auto $file >> ${file//.fasta/.aln.fa}
done

echo mafft done

