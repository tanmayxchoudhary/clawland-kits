#!/usr/bin/env python3
"""
Discrete (digital) sensor reader — DC Guardian kit.
Reads digital state from leak, smoke, and door sensors.

This is a documentation/code-quality stub showing the intended driver interface.
Replace the read_sensor() body with libgpiod or sysfs GPIO calls in production.
"""

import argparse
import json
import sys
from typing import Optional


def read_sensor(pin: str, name: str) -> dict:
    """
    Read the digital state of a GPIO pin.

    Args:
        pin: GPIO pin identifier (e.g., 'GPIO20').
        name: Human-readable sensor name (e.g., 'leak', 'smoke', 'door_rack').

    Returns:
        dict with keys: ok, pin, name, active (boolean)
        where active=True means the alert condition is present.
    """
    # ── Production implementation ──
    # For libgpiod v2:
    #   chip = gpiod.Chip('gpiochip0')
    #   line = chip.get_line(pin_number)
    #   value = line.get_value()
    #
    # For sysfs:
    #   gpio_N = int(pin.replace('GPIO', ''))
    #   with open(f'/sys/class/gpio/gpio{gpio_N}/value') as f:
    #       value = int(f.read().strip())
    #
    # active_high is configured in skill.yaml:
    #   leak → active_high=true (HIGH=wet)
    #   smoke → active_high=true (HIGH=smoke)
    #   door_rack → active_high=false (LOW=door closed)

    return {
        "ok": True,
        "pin": pin,
        "name": name,
        "active": False,  # stub: all normal
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read discrete sensor state (DC Guardian kit)"
    )
    parser.add_argument("--pin", required=True, help="GPIO pin (e.g., GPIO20)")
    parser.add_argument("--name", required=True,
                        help="Sensor name (leak, smoke, door_rack, door_room)")
    args = parser.parse_args()

    result = read_sensor(args.pin, args.name)
    print(json.dumps(result))

    if not result.get("ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
