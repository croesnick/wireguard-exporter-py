FROM python:3.9-slim

LABEL maintainer Carsten Rösnick-Neugebauer
COPY . .
RUN pip3 install -U poetry && poetry build && pip3 install -U dist/wireguard_exporter_py-*.whl

EXPOSE 9586/tcp
CMD wireguard-exporter-py
