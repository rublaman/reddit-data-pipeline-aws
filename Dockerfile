FROM apache/airflow:2.10.1-python3.10

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
