#!/usr/bin/env python3
"""
DHT22 (AM2302) temperature/humidity sensor reader — DC Guardian kit.

This is a documentation/code-quality stub showing the intended driver interface.
Replace the read_sensor() body with board-specific GPIO bit-bang or kernel driver
calls in production.

Protocol: DHT22 uses a single-wire proprietary protocol:
  1. MCU pulls DATA LOW for ~18 ms (start signal)
  2. MCU releases DATA, pulls HIGH for ~40 µs
  3. DHT22 responds with 80 µs LOW + 80 µs HIGH
  4. 40 data bits: 50 µs LOW + 26-28 µs HIGH = 0, 70 µs HIGH = 1
  5. Data: 16 bit humidity, 16 bit temperature, 8 bit checksum
"""

import argparse
import json
import sys
from typing import Optional


def read_sensor(pin: str) -> dict:
    """
    Read temperature and humidity from a DHT22 sensor.

    Args:
        pin: GPIO pin identifier (e.g., 'GPIO17').

    Returns:
        dict with keys: ok, pin, name, temperature_c, humidity_percent
        or ok=False with error message on failure.
    """
    # ── Production implementation should ──
    # 1. Export GPIO and set direction=out
    # 2. Drive LOW for 18 ms
    # 3. Switch to input and time pulse widths
    # 4. Decode 40-bit frame
    # 5. Validate checksum
    # 6. Return ±0.5°C accurate values
    #
    # For linux sysfs: /sys/class/gpio/gpio{N}/direction, /value
    # For libgpiod: gpiod.Chip('gpiochip0').get_line(pin_number)
    # For kernel driver: /sys/bus/iio/devices/iio:deviceX/in_temp_input

    # stub: return simulated value
    import random
    # simulate real-world noise (±0.3°C, ±2% RH)
    return {
        "ok": True,
        "pin": pin,
        "temperature_c": round(24.5 + random.uniform(-0.3, 0.3), 1),
        "humidity_percent": round(46.0 + random.uniform(-2, 2), 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read DHT22 temperature/humidity sensor (DC Guardian kit)"
    )
    parser.add_argument("--pin", required=True, help="GPIO pin (e.g., GPIO17)")
    parser.add_argument("--name", default="dht22", help="Sensor label (e.g., room, hvac)")
    args = parser.parse_args()

    result = read_sensor(args.pin)
    result["name"] = args.name
    print(json.dumps(result))

    if not result.get("ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
