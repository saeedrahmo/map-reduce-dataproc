# coen424-assignment-2

Dataproc zones
https://cloud.google.com/compute/docs/regions-zones#available

Create a cluster
gcloud dataproc clusters create cluster-coen424-a-2 --bucket bucket-coen424-a-2 --zone northamerica-northeast2-a --region northamerica-northeast2 --num-workers 2 --master-machine-type n1-standard-4 --worker-machine-type n1-standard-4

Build sample wordcount 
mvn clean package -Dbigtable.projectID=coen424-a-2 -Dbigtable.instanceID=bigtable-coen424-a-2

Execute the job
./cluster.sh start cluster-coen424-a-2

