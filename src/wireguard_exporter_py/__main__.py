"""Wireguard exporter."""


import os
import time
from prometheus_client import start_http_server, Gauge
from wireguard_exporter_py import wireguard


class Metrics:
    """Wrapper for periodic fetch of Wireguard metrics from local process."""

    def __init__(self, polling_interval_seconds=5):
        self.polling_interval_seconds = polling_interval_seconds

        self.alive = Gauge(
            "wireguard_alive", "Whether or not fetching wireguard metrics succeeded"
        )
        self.current_connections = Gauge(
            "wireguard_connections_current", "Current open Wireguard connections"
        )

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        """
        Get Wireguard metrics and refresh Prometheus metrics with new values.
        """

        status = wireguard.fetch()
        if status:
            self.alive.set(1)
            self.current_connections.set(len(status.peers))
        else:
            self.alive.set(0)
            self.current_connections.set(0)


def main():
    polling_interval_seconds = int(
        os.getenv("WIREGUARD_EXPORTER_POLLING_INTERVAL_SECONDS", "5")
    )
    exporter_port = int(os.getenv("WIREGUARD_EXPORTER__PORT", "9586"))

    metrics = Metrics(polling_interval_seconds=polling_interval_seconds)
    start_http_server(exporter_port)

    metrics.run_metrics_loop()


if __name__ == "__main__":
    main()  # pragma: no cover
