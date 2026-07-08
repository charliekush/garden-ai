/**
 * @file calibration.h
 * @brief Raw ADC to engineering unit conversion declarations.
 * @date 2026-07-07
 */

#ifndef CALIBRATION_H
#define CALIBRATION_H

#include <stdint.h>

/**
 * @brief Convert a raw soil moisture ADC reading to percent.
 *
 * TODO: implement the moisture sensor calibration curve.
 *
 * @param raw Raw ADC reading from sensors_read_soil_moisture_raw().
 * @return Soil moisture in percent.
 */
double calibration_raw_to_moisture_percent(uint16_t raw);

/**
 * @brief Convert a raw pH ADC reading to a pH value.
 *
 * TODO: implement the pH sensor calibration curve.
 *
 * @param raw Raw ADC reading from sensors_read_ph_raw().
 * @return pH value.
 */
double calibration_raw_to_ph(uint16_t raw);

#endif /* CALIBRATION_H */
