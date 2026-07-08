/**
 * @file sensors.h
 * @brief ADC read declarations for the soil moisture and pH sensors.
 * @date 2026-07-07
 */

#ifndef SENSORS_H
#define SENSORS_H

#include <stdint.h>

/**
 * @brief Initialize the analog inputs used for soil moisture and pH sensing.
 *
 * TODO: confirm the actual moisture/pH pin assignments and ADC resolution.
 *
 * @return 0 on success, negative errno on failure.
 */
int sensors_init(void);

/**
 * @brief Read the raw ADC value from the soil moisture sensor channel.
 *
 * TODO: implement via analogRead() on the moisture pin.
 *
 * @param out_raw Non-null pointer to store the raw ADC reading.
 * @return 0 on success, negative errno on failure.
 */
int sensors_read_soil_moisture_raw(uint16_t *out_raw);

/**
 * @brief Read the raw ADC value from the pH sensor channel.
 *
 * TODO: implement via analogRead() on the pH pin.
 *
 * @param out_raw Non-null pointer to store the raw ADC reading.
 * @return 0 on success, negative errno on failure.
 */
int sensors_read_ph_raw(uint16_t *out_raw);

#endif /* SENSORS_H */
