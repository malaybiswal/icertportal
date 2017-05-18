#max=899999  809274
min=1211869
#min = 1203100
max=1505780
while [ $min -le $max ]
do
	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/mala0858/malay/python/icertProject/icertdetail4.py $min
	(( min++ ))
done

#for i in `seq 1203000 $max`

#do
#    /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/mala0858/malay/python/icertProject/icertdetail4.py $i
#done
