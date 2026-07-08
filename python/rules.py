"""Per-species reference ranges and rule-based fusion of vision + sensor data.

TODO: populate SPECIES_REFERENCE with target moisture/pH ranges per species
and implement evaluate() to fuse infer.py output with sensor_bridge.py
readings.
"""

from __future__ import annotations

from typing import Any

SPECIES_REFERENCE: dict[str, dict[str, Any]] = {
    # TODO: fill in per-species reference ranges, e.g.:
    # "tomato": {"moisture_pct": (60, 80), "ph": (6.0, 6.8)},
}


def evaluate(species: str, health_result: Any, sensor_reading: Any) -> dict:
    """Fuse vision inference and sensor readings into a final assessment.

    TODO: implement rule engine comparing sensor_reading and health_result
    against SPECIES_REFERENCE for the detected species.

    Args:
        species: Detected species label from infer.run_models().
        health_result: Health model output from infer.run_models().
        sensor_reading: Decoded sensor_bridge.SensorReading.

    Returns:
        Dict describing the fused plant status.
    """
    raise NotImplementedError
