#!/usr/bin/env python3
"""
SCT-013 + ADS1115 non-invasive AC current clamp reader — DC Guardian kit.

Reads current from an SCT-013-030 (30A) split-core current transformer
via an ADS1115 16-bit I²C ADC.

This is a documentation/code-quality stub showing the intended driver interface.
Replace with smbus2 / adafruit-circuitpython-ads1x15 calls in production.

Calibration:
  SCT-013-030 output: 1V AC at 30A (rated), with 1.5V DC bias.
  ADS1115 range: ±4.096V (default), 16-bit signed = −32768 to +32767.
  At zero current: ADC reading ≈ 16384 (1.5V DC bias).
  At 30A: ADC reading ≈ 16384 ± 8192 (1.5V ± 1.0V AC peak).
  
  Conversion formula:
    current_A = (adc_raw - 16384) * (30.0 / 8192)
"""

import argparse
import json
import math
import sys
from typing import Optional

# SCT-013-030 calibration constants
ADC_ZERO_CURRENT = 16384     # Mid-scale at 1.5V bias
ADC_FULL_SCALE = 8192        # ±8192 counts = ±1.0V = 30A
SCT_RATED_CURRENT = 30.0     # Amps at full scale

# ADS1115 I²C address and registers
ADS1115_ADDRESS = 0x48
ADS1115_REG_CONVERSION = 0x00
ADS1115_REG_CONFIG = 0x01

# Configuration register bits (for reference)
ADS1115_CONFIG_OS_SINGLE = 0x8000   # Start single conversion
ADS1115_CONFIG_MUX_AIN0_GND = 0x0000  # A0 vs GND
ADS1115_CONFIG_GAIN_4_096V = 0x0200   # ±4.096V
ADS1115_CONFIG_MODE_SINGLE = 0x0100   # Single-shot mode
ADS1115_CONFIG_DR_860_SPS = 0x00E0    # 860 samples/second
ADS1115_CONFIG_COMP_QUE_DISABLE = 0x0003  # Disable comparator


def read_current() -> dict:
    """
    Read branch circuit current from SCT-013-030 via ADS1115.

    Returns:
        dict with keys: ok, current_A, raw_adc, timestamp
        or ok=False with error message on failure.
    """
    # ── Production implementation (smbus2) ──
    # import smbus2
    # bus = smbus2.SMBus(1)  # I2C bus 1 (or 0 for LicheeRV Nano)
    #
    # # Configure ADS1115: single-shot, AIN0 vs GND, ±4.096V, 860 SPS
    # config = (ADS1115_CONFIG_OS_SINGLE |
    #           ADS1115_CONFIG_MUX_AIN0_GND |
    #           ADS1115_CONFIG_GAIN_4_096V |
    #           ADS1115_CONFIG_MODE_SINGLE |
    #           ADS1115_CONFIG_DR_860_SPS |
    #           ADS1115_CONFIG_COMP_QUE_DISABLE)
    # bus.write_word_data(ADS1115_ADDRESS, ADS1115_REG_CONFIG, config)
    # time.sleep(0.01)  # Wait for conversion
    # raw = bus.read_word_data(ADS1115_ADDRESS, ADS1115_REG_CONVERSION)
    #
    # # ADS1115 returns MSB first; swap bytes for signed 16-bit
    # raw = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)
    # if raw >= 32768:
    #     raw -= 65536  # Convert to signed
    #
    # # Convert to amperage
    # current = (raw - ADC_ZERO_CURRENT) * (SCT_RATED_CURRENT / ADC_FULL_SCALE)
    # current = abs(current)  # AC — take absolute value

    # stub: simulate reading
    import random
    import time
    raw = ADC_ZERO_CURRENT + random.randint(-500, 500)
    current = abs((raw - ADC_ZERO_CURRENT) * (SCT_RATED_CURRENT / ADC_FULL_SCALE))

    return {
        "ok": True,
        "current_A": round(current, 2),
        "raw_adc": raw,
        "timestamp": time.time(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read SCT-013-030 current clamp via ADS1115 (DC Guardian kit)"
    )
    parser.parse_args()

    result = read_current()
    print(json.dumps(result))

    if not result.get("ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
