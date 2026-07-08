/**
 * @file sketch.ino
 * @brief Arduino sketch entry point: samples the soil moisture and pH
 * sensors on the MCU and exposes the latest reading to the MPU over the
 * Arduino_RouterBridge RPC link.
 * @date 2026-07-07
 */

#include "Arduino_RouterBridge.h"

#include "calibration.h"
#include "sensors.h"

#define SAMPLE_PERIOD_MS 1000

/**
 * @brief Latest moisture reading in percent, refreshed once per
 * SAMPLE_PERIOD_MS in loop() and served to the MPU via the
 * "get_moisture_percent" Bridge function.
 */
static double latest_moisture_percent = 0.0;

/**
 * @brief Latest pH reading, refreshed once per SAMPLE_PERIOD_MS in loop()
 * and served to the MPU via the "get_ph" Bridge function.
 */
static double latest_ph = 0.0;

/**
 * @brief Latest fault status. 0 means OK. Refreshed once per
 * SAMPLE_PERIOD_MS in loop() and served to the MPU via the "get_status"
 * Bridge function.
 */
static uint8_t latest_status = 0;

/**
 * @brief Bridge-provided function returning the latest moisture reading.
 *
 * Called from Python via Bridge.call("get_moisture_percent").
 *
 * @return Latest soil moisture in percent.
 */
static double get_moisture_percent()
{
    return latest_moisture_percent;
}

/**
 * @brief Bridge-provided function returning the latest pH reading.
 *
 * Called from Python via Bridge.call("get_ph").
 *
 * @return Latest pH value.
 */
static double get_ph()
{
    return latest_ph;
}

/**
 * @brief Bridge-provided function returning the latest fault status.
 *
 * Called from Python via Bridge.call("get_status").
 *
 * @return Latest fault status. 0 means OK.
 */
static uint8_t get_status()
{
    return latest_status;
}

/**
 * @brief Arduino setup(): initializes sensors and registers the Bridge
 * functions the MPU polls for sensor data.
 */
void setup()
{
    sensors_init();

    Bridge.begin();
    Bridge.provide("get_moisture_percent", get_moisture_percent);
    Bridge.provide("get_ph", get_ph);
    Bridge.provide("get_status", get_status);
}

/**
 * @brief Arduino loop(): samples both sensors and refreshes the readings
 * exposed to the MPU every SAMPLE_PERIOD_MS.
 */
void loop()
{
    uint16_t moisture_raw = 0;
    uint16_t ph_raw = 0;

    sensors_read_soil_moisture_raw(&moisture_raw);
    sensors_read_ph_raw(&ph_raw);

    latest_moisture_percent = calibration_raw_to_moisture_percent(moisture_raw);
    latest_ph = calibration_raw_to_ph(ph_raw);
    latest_status = 0;

    delay(SAMPLE_PERIOD_MS);
}
