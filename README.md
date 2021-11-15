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

