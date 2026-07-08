# Garden AI

Edge AI plant-monitoring project for the Arduino Uno Q, developed via
`arduino-app-cli` instead of App Lab. Split across its two processors:

- `sketch/` — MCU sketch (`arduino:zephyr:unoq` FQBN). Real-time sampling of
  soil moisture + pH, exposed to the MPU over the Arduino_RouterBridge RPC
  link (`get_moisture_percent`, `get_ph`, `get_status`).
- `python/` — MPU app (Debian on the Qualcomm side). USB webcam capture
  (Logitech 1080p Pro Stream Webcam over V4L2, connected alongside board
  power through a USB splitter), TFLite species/health inference, sensor
  fusion via `sensor_bridge.py`, and orchestration.

`app.yaml` at the repo root is the App Lab/CLI app manifest tying the two
halves together.

## Deploying

Files are synced to the board over SSH with rsync and run via
`arduino-app-cli`. From VS Code, run the **Uno Q: Deploy** task (stops the
app, rsyncs the project, restarts it). First time only, run
**Uno Q: Init Remote Directory** to create the app folder on the board. Use
**Uno Q: View Logs** to tail Python's log output.

Deploy target and remote path are set via the `UNOQ_HOST`/`UNOQ_REMOTE_DIR`
env vars in `.vscode/tasks.json`.

Equivalent manual commands:

```
ssh arduino@chuckduino.local "mkdir -p ~/ArduinoApps/garden-ai"   # once
rsync -avz --delete -e ssh ./ arduino@chuckduino.local:~/ArduinoApps/garden-ai/
ssh arduino@chuckduino.local "arduino-app-cli app start ~/ArduinoApps/garden-ai"
ssh arduino@chuckduino.local "arduino-app-cli app logs ~/ArduinoApps/garden-ai"
ssh arduino@chuckduino.local "arduino-app-cli app stop ~/ArduinoApps/garden-ai"
```

## sketch (MCU)

Compiled and flashed as part of `arduino-app-cli app start`; no separate
build step needed. `sketch/sketch.yaml` declares the board FQBN and
libraries.

## python (MPU)

Local editing only, no local run — `python/main.py` calls `App.run()`,
which requires the on-device `arduino.app_utils` runtime. For local syntax
checking:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r python/requirements.txt
```

Drop `species.tflite` and `health.tflite` into `python/models/` before
running inference.
