"""Get information from running Wireguard instance."""

from dataclasses import dataclass
import datetime
import subprocess
from typing import List, Optional


@dataclass
class Peer:
    public_key: str
    preshared_key: str
    endpoint: str
    allowed_ips: str
    latest_handshake: datetime.datetime
    transfer_rx: int
    transfer_tx: int
    persistent_keepalive: str


@dataclass
class Info:
    public_key: str
    listen_port: int
    fwmark: str

    peers: List[Peer]


def parse_peer(line: str) -> Optional[Peer]:
    parts = line.split("\t")
    return Peer(
        public_key=parts[0],
        preshared_key=parts[1],
        endpoint=parts[2],
        allowed_ips=parts[3],
        latest_handshake=datetime.datetime.fromtimestamp(float(parts[4])),
        transfer_rx=int(parts[5]),
        transfer_tx=int(parts[6]),
        persistent_keepalive=parts[7],
    )


def parse(raw: str) -> Optional[Info]:
    lines = raw.splitlines()

    peers = [parse_peer(line) for line in lines[1:]]
    peers = [peer for peer in peers if peer]

    parts = lines[0].split("\t")

    return Info(
        public_key=parts[1],
        listen_port=int(parts[2]),
        fwmark=parts[3],
    )


def fetch() -> Optional[Info]:
    result = subprocess.run(
        ["wg", "show", "wg0", "dump"], shell=True, check=False, capture_output=True
    )

    if result.returncode != 0:
        return None

    output = result.decode("utf-8")
    return parse(output)
