FROM apache/airflow:2.6.0

USER root

RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins /opt/airflow/config  && \
    chown -R 50000:50000 /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins /opt/airflow/config

COPY opt/spark/jars/gcs-connector-hadoop3-latest.jar /opt/bitnami/spark/jars/
COPY opt/spark/jars/spark-3.4-bigquery-0.37.0.jar /opt/bitnami/spark/jars/
RUN chown -R 1001:1001 /opt/bitnami/spark/jars

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

USER airflow

RUN pip install 'pyarrow>=10.0.1,<10.1.0'
RUN pip install apache-airflow-providers-apache-spark
