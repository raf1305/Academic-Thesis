for j in *.FASTA.pssm
do
	python probability.py $j
done
for i in *.prob.txt
do
	python bigram.py $i
	rm $i
done

