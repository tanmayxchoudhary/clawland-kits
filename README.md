# Clawland Kits

**Open hardware sensor kit designs — BOMs, wiring diagrams, drivers, and pre-built images for edge AI monitoring scenarios.**

> Part of the [Clawland](https://github.com/Clawland-AI) ecosystem.

---

## Overview

Clawland Kits provides **ready-to-build hardware recipes** that pair Claw agents with sensors to replace expensive human monitoring jobs. Each kit includes a complete Bill of Materials, wiring diagram, driver code, and PicClaw skill configuration.

## Available Kits

| Kit | Sensors | Board | Total Cost | Replaces |
|-----|---------|-------|-----------|----------|
| [**DC Guardian**](kits/dc-guardian/) | DHT22 + Smoke + Water | LicheeRV-Nano | ~$86.58 | $48K/yr datacenter night shift |
| **Aqua Watch** | pH + DO + Temp + Turbidity | LicheeRV-Nano | ~$133 | $30K/yr fish pond patrol |
| **Green Thumb** | Soil + Temp/Humidity + Light + CO2 | LicheeRV-Nano | ~$95 | $18K/yr greenhouse attendant |
| **Cold Chain** | DS18B20 + GPS + 4G | ESP32-S3 + PicClaw | ~$62 | $12K/yr cold chain inspector |
| **Elder Guardian** | PIR + Door + mmWave | LicheeRV-Nano | ~$30 | $900/yr care subscription |
| **Power Monitor** | SCT-013 + ADS1115 | ESP32-S3 + PicClaw | ~$45 | $6K/yr energy auditor |
| **Air Quality** | PMS5003 + SGP30 + BME280 | LicheeRV-Nano | ~$78 | $24K/yr environmental monitor |
| **Water Watch** | Flow + Pressure + pH | ESP32-S3 + PicClaw | ~$85 | $15K/yr water plant operator |
| **Machine Pulse** | Vibration + Current + Temp | ESP32-S3 + PicClaw | ~$55 | $36K/yr maintenance tech |
| **Solar Shepherd** | Irradiance + Temp + Current | ESP32-S3 + PicClaw | ~$48 | $8K/yr solar farm inspector |

## Kit Structure

Each kit directory contains:

```
kits/dc-guardian/
├── README.md           # Overview, use case, ROI calculation
├── BOM.md              # Complete parts list with purchase links
├── WIRING.md           # Connection diagram (Fritzing + text)
├── wiring.fzz          # Fritzing source file
├── drivers/            # Sensor driver code
│   ├── read_dht22.py
│   ├── read_ds18b20.py
│   ├── read_discrete.py
│   └── read_sct013.py
├── skill.yaml          # PicClaw skill configuration
├── alerts.yaml         # Alert thresholds and escalation rules
├── TROUBLESHOOTING.md  # Edge-case diagnostic guide
├── SAFETY.md           # Compliance and safety notes
└── MAINTENANCE.md      # Long-term maintenance schedule
```

## How to Build

1. **Choose a kit** from the table above
2. **Order parts** from the BOM (links included for common suppliers)
3. **Wire it up** following the diagram
4. **Flash PicClaw** onto the board
5. **Load the skill** — `picclaw skill install <kit-name>`
6. **Configure alerts** — Edit thresholds in `alerts.yaml`

## Status

🚧 **Pre-Alpha** — First 3 kits (DC Guardian, Aqua Watch, Green Thumb) in design phase.

## Contributing

**Hardware contributions are especially welcome!** See the [Sensor Kit Proposal template](https://github.com/Clawland-AI/.github/blob/main/ISSUE_TEMPLATE/sensor_kit_proposal.md) to propose a new kit.

**Core contributors share 20% of product revenue.** Read the [Contributor Revenue Share](https://github.com/Clawland-AI/.github/blob/main/CONTRIBUTOR-REVENUE-SHARE.md) terms.

## License

**CERN Open Hardware Licence Version 2 — Strongly Reciprocal (CERN-OHL-S-2.0)**

Hardware designs must remain open. See [LICENSE](LICENSE) for full terms.
