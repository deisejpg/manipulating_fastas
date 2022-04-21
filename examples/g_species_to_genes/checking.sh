#for file in *.cln.sorted.fa; do echo grep -H "'>'" $file '|' wc -l; done &> checking.sh
#either run the loop in the command line without the last bit '&> checking.sh' or
#run the bash script with 'bash checking'
grep -H '>' JQ757046.cln.sorted.fa | wc -l
grep -H '>' KF156836.cln.sorted.fa | wc -l
grep -H '>' KU878156.cln.sorted.fa | wc -l
grep -H '>' KX904873.cln.sorted.fa | wc -l
grep -H '>' MF359935.cln.sorted.fa | wc -l
grep -H '>' MF359937.cln.sorted.fa | wc -l
grep -H '>' MF359943.cln.sorted.fa | wc -l
grep -H '>' MF359952.cln.sorted.fa | wc -l
grep -H '>' MN078090.cln.sorted.fa | wc -l
grep -H '>' MN711645.cln.sorted.fa | wc -l
grep -H '>' MZ073672.cln.sorted.fa | wc -l
grep -H '>' NC_007898.cln.sorted.fa | wc -l
grep -H '>' NC_014697.cln.sorted.fa | wc -l
grep -H '>' NC_019616.cln.sorted.fa | wc -l
grep -H '>' NC_024663.cln.sorted.fa | wc -l
grep -H '>' NC_026690.cln.sorted.fa | wc -l
grep -H '>' NC_026691.cln.sorted.fa | wc -l
grep -H '>' NC_030786.cln.sorted.fa | wc -l
grep -H '>' NC_030789.cln.sorted.fa | wc -l
grep -H '>' NC_031376.cln.sorted.fa | wc -l
grep -H '>' NC_031428.cln.sorted.fa | wc -l
grep -H '>' NC_034914.cln.sorted.fa | wc -l
grep -H '>' NC_035705.cln.sorted.fa | wc -l
grep -H '>' NC_035709.cln.sorted.fa | wc -l
grep -H '>' NC_036052.cln.sorted.fa | wc -l
grep -H '>' NC_036306.cln.sorted.fa | wc -l
grep -H '>' NC_037472.cln.sorted.fa | wc -l
grep -H '>' NC_039973.cln.sorted.fa | wc -l
grep -H '>' NC_041473.cln.sorted.fa | wc -l
grep -H '>' NC_041602.cln.sorted.fa | wc -l
grep -H '>' NC_048520.cln.sorted.fa | wc -l
grep -H '>' NC_053764.cln.sorted.fa | wc -l
grep -H '>' NC_059012.cln.sorted.fa | wc -l
grep -H '>' NC_059942.cln.sorted.fa | wc -l
grep -H '>' OL450428.cln.sorted.fa | wc -l