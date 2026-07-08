/**
 * @file sensors.cpp
 * @brief ADC read stubs for the soil moisture and pH sensors.
 * @date 2026-07-07
 */

#include "sensors.h"

#include <Arduino.h>

// TODO: confirm the actual moisture/pH analog pin assignments.
#define MOISTURE_PIN A0
#define PH_PIN A1

int sensors_init(void)
{
    /* TODO: set pin mode / ADC resolution if the defaults are not suitable. */
    return 0;
}

int sensors_read_soil_moisture_raw(uint16_t *out_raw)
{
    /* TODO: trigger an analogRead() on MOISTURE_PIN and store the result. */
    return 0;
}

int sensors_read_ph_raw(uint16_t *out_raw)
{
    /* TODO: trigger an analogRead() on PH_PIN and store the result. */
    return 0;
}
