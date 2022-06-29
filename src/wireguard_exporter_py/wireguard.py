"""Get information from running Wireguard instance.

For more information about the fields, see <https://manpages.debian.org/unstable/wireguard-tools/wg.8.en.html#show>.
"""

from dataclasses import dataclass
import datetime
import re
import subprocess
from typing import List, Optional


@dataclass
class Peer:
    endpoint: str
    allowed_ips: str
    latest_handshake: datetime.datetime
    transfer_rx: int
    transfer_tx: int
    persistent_keepalive: str


@dataclass
class Info:
    listen_port: int
    fwmark: str

    peers: List[Peer]


def parse_peer(line: str) -> Optional[Peer]:
    """Parses a peer line of the wg show dump output into an object.

    ## Examples

        >>> line = "whuM9vKf/publickey=	TO8vy/LuK7E2k/prehared/key=	1.2.3.4:28415	10.6.0.2/32	1656493413	640043784	6228128716	off"
        >>> parse_peer(line)  # doctest: +NORMALIZE_WHITESPACE
        Peer(endpoint='1.2.3.4:28415', allowed_ips='10.6.0.2/32', latest_handshake=datetime.datetime(2022, 6, 29, 11, 3, 33), transfer_rx=640043784, transfer_tx=6228128716, persistent_keepalive='off')
    """
    parts = re.split(r"\s+", line)
    return Peer(
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

    parts = re.split(r"\s+", lines[0])

    return Info(
        listen_port=int(parts[2]),
        fwmark=parts[3],
        peers=peers,
    )


def fetch() -> Optional[Info]:
    result = subprocess.run(
        ["wg", "show", "wg0", "dump"], shell=True, check=False, capture_output=True
    )

    if result.returncode != 0:
        return None

    output = result.decode("utf-8")
    return parse(output)
