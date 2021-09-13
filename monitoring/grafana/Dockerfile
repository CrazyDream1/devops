ARG GRAFANA_VERSION
FROM grafana/grafana:${GRAFANA_VERSION}

ARG NGINX_GRAFANA_HOST
USER root
COPY grafana.ini /etc/grafana/grafana.ini
RUN sed -i "s/%NGINX_GRAFANA_HOST%/granafa/" /etc/grafana/grafana.ini