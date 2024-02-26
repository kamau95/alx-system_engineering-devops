#!/bin/bash
#illustration of  untill loop at work
i=1
n=13
until [ $i -gt $n ]
do
	echo "best school"
	(( i++ ))
done
