FROM python:3.7-buster

LABEL maintainer Carsten Rösnick-Neugebauer

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
COPY . .
RUN pip3 install -U poetry && poetry build && pip3 install -U dist/wireguard_exporter_py-*.whl

EXPOSE 9586/tcp
CMD wireguard-exporter-py
