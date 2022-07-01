FROM python:3.9-slim-buster

LABEL maintainer Carsten Rösnick-Neugebauer

COPY . .
RUN apt update -y && apt install -y rustc gcc musl-dev python3-dev libffi-dev openssl libssl-dev
RUN pip3 install -U poetry && poetry build && pip3 install -U dist/wireguard_exporter_py-*.whl

EXPOSE 9586/tcp
CMD wireguard-exporter-py
