#####################
######  bulky  ######
#####################
ts=GramPotter.py

source export.sh

echo -n "down? default is [50], if you ok enter, otherwise put something "
read ct

echo -n "proceed preference? default is [n] No DL, if you ok enter, otherwise put something "
read cz

while read p; do
	echo $p
	python $ts "$p" $ct $cz
done < where.txt


 
