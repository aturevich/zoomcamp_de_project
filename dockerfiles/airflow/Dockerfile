FROM apache/airflow:2.6.0

USER root

RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins /opt/airflow/config  && \
    chown -R 50000:50000 /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins /opt/airflow/config

USER airflow

RUN pip install 'pyarrow>=10.0.1,<10.1.0'
