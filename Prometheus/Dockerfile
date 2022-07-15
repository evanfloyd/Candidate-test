FROM bitnami/prometheus:2.37.0

EXPOSE 9090
RUN sed -i "s|localhost:9090|host.docker.internal:5000|g" /opt/bitnami/prometheus/conf/prometheus.yml
ENTRYPOINT [ "/opt/bitnami/prometheus/bin/prometheus" ]
CMD [ "--config.file=/opt/bitnami/prometheus/conf/prometheus.yml", "--storage.tsdb.path=/opt/bitnami/prometheus/data", "--web.console.libraries=/opt/bitnami/prometheus/conf/console_libraries", "--web.console.templates=/opt/bitnami/prometheus/conf/consoles" ]