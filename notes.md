Data 
https://web.ais.dk/aisdata/
Data Description
https://web.ais.dk/aisdata/!_README_information_CSV_files.

tdb add description of terraform and ssh setup
command to copy file

vm firewell rule added

sudo usermod -a -G docker $USER
/bin/bash: wget: command not found
sudo wget --version
sudo apt-get install wget

sudo chown -R 50000:50000 ./logs ./dags ./plugins ### Modify it, folder will be pulled from github, needs to give only rights 

docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow db upgrade



docker-compose run airflow-webserver airflow users create \
    --username admin \
    --firstname artyom \
    --lastname tu \
    --role Admin \
    --email cratosartyom@gmail.com

create service account for airflow
    mkdir -p ./dags ./logs ./plugins ./config
    sudo chown -R Artyom:Artyom /home/Artyom/dags
    sudo chmod -R ugo+rw /home/Artyom/dags

dag_file_name_sensor



```
docker system prune -a
sudo docker-compose up --build -d
sudo usermod -aG docker $USER
```

35.184.112.30:8080



sudo mkdir -p ./opt/airflow/dags ./opt/airflow/logs ./opt/airflow/plugins ./opt/airflow/config
sudo chown -R 50000:50000 ./opt/airflow/dags ./opt/airflow/logs ./opt/airflow/plugins ./opt/airflow/config 

sudo su -

sudo chown -R $USER ./opt/


docker system prune -a
docker-compose logs airflow-webserver
docker logs 1fb880b97628 | grep "volume"

sudo docker-compose up --build -d
do
sudo systemctl restart sshd

docker exec -it b87bae0e97a0 /bin/bash
spark-submit \
--jars /opt/bitnami/spark/jars/gcs-connector-hadoop3-latest.jar \
/opt/bitnami/spark-jobs/spark_job.py \
--inputPath gs://ships-data-bucket-1fcd/test_data.zip \
--outputTable ships-data-eda:ships_ds.ships_table

docker exec -it fce0c2ebd288 ls -l /opt/bitnami/spark/jars | grep gcs


spark-submit \
--jars /opt/bitnami/spark/jars/spark-3.4-bigquery-0.37.0.jar \
--conf spark.executor.cores=1 \
/opt/bitnami/spark-jobs/spark_job.py \
gs://ships-data-bucket-1fcd/small_test_data.csv \
ships-data-eda:ships_ds.ships_table

docker system prune -a \
docker-compose up --build -d



spark-submit \
--master spark://spark-master:7077 \
--jars /opt/bitnami/spark/jars/gcs-connector-hadoop3-latest.jar,/opt/bitnami/spark/jars/spark-3.4-bigquery-0.37.0.jar \
--conf spark.hadoop.fs.gs.impl=com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem \
--conf spark.hadoop.fs.gs.auth.service.account.enable=true \
--conf spark.hadoop.fs.gs.auth.service.account.json.keyfile=/opt/bitnami/config/gcp-key.json \
--conf spark.executor.cores=1 /opt/bitnami/spark-jobs/spark_job.py gs://ships-data-bucket-1fcd/small_test_data.csv ships-data-eda:ships_ds.ships_table