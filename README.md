# coen424-assignment-2

Dataproc zones
https://cloud.google.com/compute/docs/regions-zones#available

Create a cluster
gcloud dataproc clusters create cluster-coen424-a-2 --bucket bucket-coen424-a-2 --zone northamerica-northeast2-a --region northamerica-northeast2 --num-workers 2 --master-machine-type n1-standard-4 --worker-machine-type n1-standard-4

Build sample wordcount 
mvn clean package -Dbigtable.projectID=coen424-a-2 -Dbigtable.instanceID=bigtable-coen424-a-2

Execute the job
./cluster.sh start cluster-coen424-a-2

Dataproc wordcount example:
hdfs dfs -mkdir /wordcountfiles
hdfs dfs -put pg20417.txt /wordcountfiles/
ls /usr/lib/hadoop-mapreduce/
pwd
mkdir tmp
cp /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar .
cd tmp
cp ../hadoop-mapreduce-examples.jar .
unzip hadoop-mapreduce-examples.jar 
yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /wordcountfiles/ /tmp/result/
hdfs dfs -ls /tmp/result/
hdfs dfs -get /tmp/result* ./tmp/.

Python wordcount:

/usr/lib/hadoop/hadoop-streaming.jar

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapred.jab.name="Streaming wordCount rating" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options='-k2nr' \
    -D stream.num.map.output.key.fields=2 \
    -D mapred.map.tasks=1 \
    -D mapreduce.job.reduces=1 \
    -files mapper2.py,reducer2.py \
    -mapper "python mapper2.py" \
    -reducer "python reducer2.py" \
    -input /user/jovyan/assignment0_1563877099149160 \
    -output ${OUT_DIR} > /dev/null
    
bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file /home/hduser/mapper.py    -mapper /home/hduser/mapper.py \
-file /home/hduser/reducer.py   -reducer /home/hduser/reducer.py \
-input /user/hduser/gutenberg/* -output /user/hduser/gutenberg-output

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /mypy/mapper.py    -mapper /mypy/mapper.py \
-file /mypy/reducer.py   -reducer /mypy/reducer.py \
-input /wordcountfiles/ -output /tmp/result/

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -file mypy/mapper.py -mapper mypy/mapper.py -file mypy/reducer.py -reducer mypy/reducer.py -input /wordcountfiles/ -output /tmp/result

more part-00000
realpath part-00000

https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
