#!/bin/bash

# start-dfs.sh
# start-yarn.sh

# export PATH=$PATH:$PWD/bin:$PWD/sbin

hadoop fs -rm -f -R /bigdata1
hadoop fs -rm -f -R /bigdata2 /bigdata3 /bigdata4

hadoop fs -mkdir /bigdata1
hadoop fs -put ./star2002-full.csv /bigdata1

echo "PUT"

HADOOP_JAR="share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar"

hadoop jar $HADOOP_JAR \
    -input /bigdata1 \
    -output /bigdata2 \
    -mapper "python2 map1.py" \
    -reducer "python2 reduce1.py" \
    -file map1.py \
    -file reduce1.py

echo "TASK 1 DONE"

hadoop fs -cat /bigdata2/part-00000 > quantiles

hadoop jar $HADOOP_JAR \
   -input /bigdata1 \
   -output /bigdata3 \
   -mapper "python2 map2.py" \
   -reducer "python2 reduce2.py" \
   -file ./map2.py \
   -file ./reduce2.py \
   -file ./quantiles

echo "TASK 2 DONE"

hadoop jar $HADOOP_JAR \
     -input /bigdata1 \
     -output /bigdata4 \
     -mapper "python2 map3.py" \
     -reducer "python2 reduce3.py" \
     -file ./map3.py \
     -file ./reduce3.py \
     -cacheFile "/bigdata2/part-00000#quantiles"

echo "TASK 3 DONE"

echo "############## RESULTS ##############"
echo 
hadoop fs -cat /bigdata2/part-00000
echo 
hadoop fs -cat /bigdata3/part-00000
echo 
hadoop fs -cat /bigdata4/part-00000
