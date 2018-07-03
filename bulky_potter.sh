#####################
######  bulky  ######
#####################
ts=GramPotter.py

source export.sh

echo -n "down? default is [20], if you ok enter, otherwise put something "
read ct

if [ "$ct" = "" ]
then
ct="20"
fi
	


echo -n "proceed preference? default is [n] No DL, if you ok enter, otherwise put something "
read cz

if [ "$cz" = "" ]
then
cz="n"
fi


while read p; do
	echo $p
	python $ts "$p" $ct $cz
done < where.txt


 
