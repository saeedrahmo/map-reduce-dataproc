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
hdfs dfs -get /tmp/result\* ./tmp/.

Python wordcount:

/usr/lib/hadoop/hadoop-streaming.jar

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
 -D mapred.job.name="Streaming wordCount rating" \
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

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapred.jab.name="Streaming batch" -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper2.py -mapper mypy/batch_mapper2.py -file mypy/batch_reducer2.py -reducer mypy/batch_reducer2.py -input /batchfiles/ -output /tmp/result12

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper2.py -mapper mypy/batch_mapper2.py -file mypy/batch_reducer2.py -reducer mypy/batch_reducer2.py -input /batchfiles/ -output /tmp/result18

bin/hadoop jar contrib/streaming/hadoop-_streaming_.jar \
-file /home/hduser/mapper.py -mapper /home/hduser/mapper.py \
-file /home/hduser/reducer.py -reducer /home/hduser/reducer.py \
-input /user/hduser/gutenberg/\* -output /user/hduser/gutenberg-output

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-file /mypy/mapper.py -mapper /mypy/mapper.py \
-file /mypy/reducer.py -reducer /mypy/reducer.py \
-input /wordcountfiles/ -output /tmp/result/

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -file mypy/mapper.py -mapper mypy/mapper.py -file mypy/reducer.py -reducer mypy/reducer.py -input /wordcountfiles/ -output /tmp/result

more part-00000
realpath part-00000

https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

echo "foo foo quux labs foo bar quux" | ~/Documents/WorkSpace/Github/coen424-assignment-2/mapper.py | sort -k1,1 | ~/Documents/WorkSpace/Github/coen424-assignment-2/reducer.py

chmod +x ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_mapper.py
chmod +x ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_reducer.py

echo "39,199985900,181947520,68.09846248,51.23358797\n38,197149929,178799262,70.27986756,51.78663439\n39,196705693,177780732,71.57827558,53.00514658\n39,196705693,177780732,71.57827558,53.00514658" | ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_mapper.py

Tested successfully:

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file mypy/batch_mapper.py -mapper mypy/batch_mapper.py -file mypy/batch_reducer.py -reducer mypy/batch_reducer.py -input /batchfiles/ -output /tmp/result4

Tested successfully (sorted):

# determined to apply sorting on two fields

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper4.py -mapper mypy/batch_mapper4.py -file mypy/batch_reducer4.py -reducer mypy/batch_reducer4.py -input /batchfiles/ -output /tmp/result21

# final tested successfuly

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper.py -mapper mypy/batch_mapper.py -file mypy/batch_reducer.py -reducer mypy/batch_reducer.py -input /batchfiles/ -output /tmp/result

# calculating deviation

https://www.w3schools.com/python/python_ml_standard_deviation.asp

https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/

![Creating Hadoop cluster on Google Dataproc cloud service](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Creating%20Hadoop%20cluster%20on%20Google%20Dataproc%20cloud%20service.png
