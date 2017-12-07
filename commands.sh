hadoop fs -mkdir /bigdata1
hadoop fs -put ./star2002-full.csv /bigdata1

hadoop jar hadoop-streaming.jar \
    -input /bigdata1 \
    -output /bigdata2 \
    -mapper "python2 map1.py" \
    -reducer "python2 reduce1.py" \
    -file map1.py \
    -file reduce1.py
# hadoop jar hadoop-streaming-2.8.2.jar     -input /bigdata1     -output /bigdata2     -mapper "python2 map1.py"     -reducer "python2 reduce1.py"     -file ./map1.py     -file ./reduce1.py

hadoop fs -cat /bigdata2/part-00000 > quantiles.txt

hadoop jar hadoop-streaming-2.8.2.jar     -input /bigdata1     -output /bigdata3     -mapper "python2 map2.py"     -reducer "python2 reduce2.py"     -file ./map2.py     -file ./reduce2.py
hadoop jar hadoop-streaming-2.8.2.jar     -input /bigdata1     -output /bigdata4     -mapper "python2 map3.py"     -reducer "python2 reduce3.py"     -file ./map3.py     -file ./reduce3.py
