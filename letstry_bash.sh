#!/bin/bash

var_1=a$1 #take first peram. as table name including 'a' ex. a54 a117 etc
var_2=$1

python ./magnet.py $var_2 #executing magnet.py which take only digit as argument

#loading created text file by magnet.py and load it to MySQL database
mysql -D newuserdata -u projectuser -pankitldrpceb -e "LOAD DATA LOCAL INFILE '/home/villain/final_project/$var_2.txt' INTO TABLE $var_1 COLUMNS TERMINATED BY '\t'"

