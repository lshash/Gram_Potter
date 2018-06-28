#####################
######  bulky  ######
#####################
ts=GramPotter.py

source export.sh

echo -n "how down? "
read ct

echo -n "preference? put [n] only when testing with No DL "
read cz

while read p; do
	echo $p
	python $ts "$p" $ct $cz
done < where.txt


 
