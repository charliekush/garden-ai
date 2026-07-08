/**
 * @file calibration.cpp
 * @brief Raw ADC to engineering unit conversion stubs.
 * @date 2026-07-07
 */

#include "calibration.h"

double calibration_raw_to_moisture_percent(uint16_t raw)
{
    /* TODO: apply the moisture sensor calibration curve. */
    return 0.0;
}

double calibration_raw_to_ph(uint16_t raw)
{
    /* TODO: apply the pH sensor calibration curve. */
    return 0.0;
}
