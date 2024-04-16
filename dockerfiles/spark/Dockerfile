FROM bitnami/spark:3

USER root

COPY opt/spark/jars/gcs-connector-hadoop3-latest.jar /opt/bitnami/spark/jars/

ENV SPARK_HOME=/opt/spark
ENV SPARK_CLASSPATH=$SPARK_CLASSPATH:/opt/spark/jars/gcs-connector-hadoop3-latest.jar
