"""Fetch the latest sensor reading from the MCU over the Bridge RPC link.

Calls the functions provided by sketch/sketch.ino (get_moisture_percent,
get_ph, get_status) via arduino.app_utils.Bridge. Replaces the earlier raw
UART packet framing now that the MCU side talks Arduino_RouterBridge instead
of a hand-rolled serial protocol.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

from arduino.app_utils import Bridge


@dataclass
class SensorReading:
    """Latest sensor reading fused from the three MCU-provided Bridge calls."""

    timestamp: float
    moisture: float
    ph: float
    status: int


def read_sensors() -> SensorReading:
    """Poll the MCU over Bridge and assemble the latest SensorReading.

    TODO: confirm Bridge.call() error/timeout behavior and add retry/backoff
    for the case where the MCU sketch is still booting or unresponsive.

    Returns:
        Latest SensorReading.
    """
    moisture = Bridge.call("get_moisture_percent")
    ph = Bridge.call("get_ph")
    status = Bridge.call("get_status")
    return SensorReading(timestamp=time.time(), moisture=moisture, ph=ph, status=status)
