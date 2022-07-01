FROM python:3.9-slim-buster AS base

COPY . .

RUN apt update -y && apt install -y rustc gcc musl-dev python3-dev libffi-dev openssl libssl-dev
RUN pip3 install -U --user "cffi==1.15.0" "cryptography<3.5" && pip3 install poetry && poetry build 

################################################################################

FROM python:3.9-alpine
LABEL maintainer Carsten Rösnick-Neugebauer

COPY --from=base /root/.local /root/.local
COPY --from=base dist/wireguard_exporter_py-*.whl /root/

RUN pip3 install /root/wireguard_exporter_py-*.whl && rm -rf /root/.cache

EXPOSE 9586/tcp
CMD wireguard-exporter-py
