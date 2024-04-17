FROM bitnami/spark:3.4.2

USER root

RUN mkdir -p /bitnami/spark/conf && \
    chown -R 1001:1001 /bitnami/spark/conf && \
    chown -R 1001:1001 /opt/bitnami/spark/jars

COPY opt/spark/jars/gcs-connector-hadoop3-latest.jar /opt/bitnami/spark/jars/
COPY opt/spark/jars/spark-3.4-bigquery-0.37.0.jar /opt/bitnami/spark/jars/
RUN chown -R 1001:1001 /opt/bitnami/spark/jars

ENV SPARK_HOME=/opt/bitnami/spark
# Set classpath to include the Spark configuration directory and all JARs in the jars directory
ENV SPARK_CLASSPATH=$SPARK_HOME/conf:$SPARK_HOME/jars/*
USER 1001