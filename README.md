# Introduction

This project aims to practice the MapReduce algorithm, its implementation (by Java or Python, or C++ or other programming languages) and runtime (such as Hadoop or AWS EMR, or Azure HDInsight or MongoDB or Google Dataproc).

Google Dataproc is used as the cloudbased Hadoop cluster system. Furthermore, Python programming language is used to develop the MapReduce algorithm;  Hadoop streaming is employed which is a utility that comes with the Hadoop distribution. The utility gives the ability to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer. In other words, the technique behind Python code is that the Hadoop Streaming API passes data between the Map and Reduce code via STDIN (standard input) and STDOUT (standard output). Python’s sys.stdin to read input data and print the results to sys.stdout. Hadoop Streaming will take care of the rest.

Two pieces of Python code, a batch mapper.py as the mapper, and a batch reducer.py as the reducer. The mapper will read data from STDIN which will be the source dataset NDBench, split it into batches, and output a list of lines mapping the metric chosen to its values to STDOUT. Afterward, the reducer will read the results of batch mapper.py from STDIN (so the output format of mapper.py and the expected input format of reducer.py match) and calculate the Maximum, Minimum, Median, and Standard Deviation of the selected metric in each batch, and then output its results to STDOUT.

# Description

Dataproc zones<br />
https://cloud.google.com/compute/docs/regions-zones#available

Create a cluster<br />
gcloud dataproc clusters create cluster-coen424-a-2 --bucket bucket-coen424-a-2 --zone northamerica-northeast2-a --region northamerica-northeast2 --num-workers 2 --master-machine-type n1-standard-4 --worker-machine-type n1-standard-4

Build sample wordcount<br />
mvn clean package -Dbigtable.projectID=coen424-a-2 -Dbigtable.instanceID=bigtable-coen424-a-2

Execute the job<br />
./cluster.sh start cluster-coen424-a-2

Dataproc wordcount example:<br />
hdfs dfs -mkdir /wordcountfiles<br />
hdfs dfs -put pg20417.txt /wordcountfiles/<br />
ls /usr/lib/hadoop-mapreduce/<br />
pwd<br />
mkdir tmp<br />
cp /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar .<br />
cd tmp<br />
cp ../hadoop-mapreduce-examples.jar .<br />
unzip hadoop-mapreduce-examples.jar<br />
yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /wordcountfiles/ /tmp/result/<br />
hdfs dfs -ls /tmp/result/<br />
hdfs dfs -get /tmp/result\* ./tmp/.<br />

Python wordcount:

/usr/lib/hadoop/hadoop-streaming.jar<br />

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \<br />
 -D mapred.job.name="Streaming wordCount rating" \<br />
 -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \<br />
 -D mapreduce.partition.keycomparator.options='-k2nr' \<br />
 -D stream.num.map.output.key.fields=2 \<br />
 -D mapred.map.tasks=1 \<br />
 -D mapreduce.job.reduces=1 \<br />
 -files mapper2.py,reducer2.py \<br />
 -mapper "python mapper2.py" \<br />
 -reducer "python reducer2.py" \<br />
 -input /user/jovyan/assignment0_1563877099149160 \<br />
 -output ${OUT_DIR} > /dev/null<br />

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapred.jab.name="Streaming batch" -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper2.py -mapper mypy/batch_mapper2.py -file mypy/batch_reducer2.py -reducer mypy/batch_reducer2.py -input /batchfiles/ -output /tmp/result12

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper2.py -mapper mypy/batch_mapper2.py -file mypy/batch_reducer2.py -reducer mypy/batch_reducer2.py -input /batchfiles/ -output /tmp/result18

bin/hadoop jar contrib/streaming/hadoop-_streaming_.jar \<br />
-file /home/hduser/mapper.py -mapper /home/hduser/mapper.py \<br />
-file /home/hduser/reducer.py -reducer /home/hduser/reducer.py \<br />
-input /user/hduser/gutenberg/\* -output /user/hduser/gutenberg-output<br />

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \<br />
-file /mypy/mapper.py -mapper /mypy/mapper.py \<br />
-file /mypy/reducer.py -reducer /mypy/reducer.py \<br />
-input /wordcountfiles/ -output /tmp/result/<br />

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -file mypy/mapper.py -mapper mypy/mapper.py -file mypy/reducer.py -reducer mypy/reducer.py -input /wordcountfiles/ -output /tmp/result

more part-00000<br />
realpath part-00000<br />

https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

echo "foo foo quux labs foo bar quux" | ~/Documents/WorkSpace/Github/coen424-assignment-2/mapper.py | sort -k1,1 | ~/Documents/WorkSpace/Github/coen424-assignment-2/reducer.py

chmod +x ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_mapper.py<br />
chmod +x ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_reducer.py

echo "39,199985900,181947520,68.09846248,51.23358797\n38,197149929,178799262,70.27986756,51.78663439\n39,196705693,177780732,71.57827558,53.00514658\n39,196705693,177780732,71.57827558,53.00514658" | ~/Documents/WorkSpace/Github/coen424-assignment-2/batch_mapper.py

Tested successfully:

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.job.reduces=1 -file mypy/batch_mapper.py -mapper mypy/batch_mapper.py -file mypy/batch_reducer.py -reducer mypy/batch_reducer.py -input /batchfiles/ -output /tmp/result4

Tested successfully (sorted):

# Determined to apply sorting on two fields

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper4.py -mapper mypy/batch_mapper4.py -file mypy/batch_reducer4.<br />py -reducer mypy/batch_reducer4.py -input /batchfiles/ -output /tmp/result21

# Final tested successfuly

yarn jar /usr/lib/hadoop/hadoop-streaming.jar -D mapreduce.partition.keycomparator.options='-k2nr' -D stream.num.map.output.key.fields=2 -D mapred.map.tasks=1 -D mapreduce.job.reduces=1 -file mypy/batch_mapper.py -mapper mypy/batch_mapper.py -file mypy/batch_reducer.py <br />-reducer mypy/batch_reducer.py -input /batchfiles/ -output /tmp/result

# Calculating deviation

https://www.w3schools.com/python/python_ml_standard_deviation.asp

https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/

# Screenshots
![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Creating%20Hadoop%20cluster%20on%20Google%20Dataproc%20cloud%20service.png?raw=true "Creating Hadoop cluster on Google Dataproc cloud service")

![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Hadoop%20cluster%20nodes.png?raw=true "Hadoop cluster nodes")

![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Hadoop%20nodes%20configuration.png?raw=true "Hadoop nodes configuration")

![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Monitoring%20the%20Hadoop%20cluster.png?raw=true "Monitoring the Hadoop cluster")

![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Submission.png?raw=true "Putting files into HDFS and submitting the job")

![ScreenShot](https://github.com/saeedrahmo/coen424-assignment-2/blob/main/screenshots/Results.png?raw=true "Getting the results from HDFS")
