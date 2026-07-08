"""Orchestrator entry point: trigger -> capture -> infer -> fuse -> output.

Runs on the MPU under arduino-app-cli, which requires App.run() to start the
process and drive the user loop.

TODO: wire together capture, preprocess, infer, sensor_bridge, and rules
into the end-to-end plant monitoring pipeline.
"""

from __future__ import annotations

from arduino.app_utils import App

import capture
import infer
import preprocess
import rules
import sensor_bridge


def run_once() -> None:
    """Run a single capture -> infer -> fuse -> output cycle.

    TODO: implement the pipeline:
      1. Wait for / check the trigger condition.
      2. Capture a frame via capture.grab_frame().
      3. Preprocess the frame via preprocess.prepare_frame().
      4. Run inference via infer.run_models().
      5. Read the latest sensor_bridge.SensorReading via sensor_bridge.read_sensors().
      6. Fuse vision + sensor results via rules.evaluate().
      7. Emit/report the result.
    """
    raise NotImplementedError


def main() -> None:
    """Orchestrator main loop, driven by App.run()."""
    App.run(user_loop=run_once)


if __name__ == "__main__":
    main()
