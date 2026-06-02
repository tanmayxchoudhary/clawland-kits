# 🔄 Maintenance Schedule — DC Guardian

> **Proper maintenance ensures > 99% uptime and 5+ year sensor lifespan.**
> Budget ~$30/year for replacement parts and consumables.

---

## 📅 Periodic Maintenance Table

| Interval | Task | Details | Estimated Time |
|----------|------|---------|:--------------:|
| **Daily** | Visual check of LEDs | Green = healthy, Red = alert | 10s |
| **Daily** | Review alert history | `picclaw alert history --since 24h` | 30s |
| **Weekly** | Sensor smoke test | Run each driver script; verify non‑zero readings | 5 min |
| **Monthly** | Clean MQ‑2 sensor | Remove dust from module enclosure with compressed air | 2 min |
| **Monthly** | Check physical cables | Look for wear, loose connections, rodent damage | 5 min |
| **Quarterly** | DHT22 accuracy check | Compare against calibrated reference (e.g., BME280) | 10 min |
| **Quarterly** | DS18B20 accuracy check | Ice‑bath test (0°C) and hand warmth test (~35°C) | 10 min |
| **Quarterly** | Leak probe function test | Wet probe with damp cloth; confirm alert fires | 2 min |
| **Quarterly** | SCT‑013 calibration check | Clamp around known load; compare to reference meter | 5 min |
| **Yearly** | Battery backup check | If using UPS HAT, test battery capacity | 15 min |
| **Yearly** | Full hardware audit | Remove and inspect all connections; re‑tighten screws | 30 min |
| **Yearly** | PicClaw upgrade | `picclaw update` or re‑flash SD card | 10 min |
| **2 years** | Replace DHT22 sensors | DHT22 has limited long‑term stability (drift) | 5 min |
| **3 years** | Replace MQ‑2 module | Heater element degrades over time; sensitivity drops | 5 min |
| **5 years** | Replace board (LicheeRV Nano) | eMMC wear, capacitor aging, security updates | 15 min |

---

## 📊 Sensor Accuracy Drift Expectations

| Sensor | Initial Accuracy | After 1 Year | After 3 Years | Recalibration Method |
|--------|:----------------:|:------------:|:-------------:|---------------------|
| DHT22 (temperature) | ±0.5°C | ±1.0°C | ±2.0°C | Replace (cannot recalibrate easily) |
| DHT22 (humidity) | ±2% RH | ±4% RH | ±8% RH | Replace |
| DS18B20 | ±0.5°C | ±0.5°C | ±0.5°C | Ice‑bath offset adjustment |
| MQ‑2 | Threshold only | Check monthly | Replace | Adjust threshold pot |

---

## 🧊 DS18B20 Ice‑Bath Calibration

Use this procedure to verify ±0.5°C accuracy:

1. Fill a thermos with crushed ice.
2. Add clean water to fill the gaps (slurry consistency).
3. Submerge the DS18B20 probe at least 3cm deep.
4. Wait 2 minutes for thermal stabilization.
5. Read temperature:
   ```bash
   picclaw sensor read ds18b20_spot
   ```
6. Expected: **0.0°C ± 0.5°C**.
7. If deviation > 0.5°C:
   - Check for electrical noise on the 1‑Wire bus
   - Verify 4.7kΩ pull‑up resistor value
   - Consider replacing the probe

---

## 🧪 DHT22 Cross‑Check Procedure

1. Place a known‑accurate reference sensor (BME280, SHT31, or psychrometer) next to DHT22 #1.
2. Allow 10 minutes for equilibration.
3. Compare readings:
   ```bash
   picclaw sensor read dht22_room
   ```
4. Acceptable tolerance: **±1°C / ±5% RH**.
5. If outside tolerance: check cable, pull‑up, and consider replacement.

---

## 🔧 Firmware / Software Updates

### PicClaw Agent
```bash
# Check current version
picclaw --version

# Update
picclaw update
# Or re‑flash the SD card (recommended for major version upgrades)
```

### Kernel / System
```bash
# LicheeRV Nano runs a custom PicClaw‑optimized kernel
# Updates are delivered via PicClaw updates
picclaw update --system
```

### Configuration backups
```bash
# Backup current config
picclaw skill export dc-guardian > dc-guardian-backup.yaml

# Before major updates
tar czf dc-guardian-config-$(date +%Y%m%d).tar.gz /etc/picclaw/
```

---

## 🔋 Power Supply Maintenance

| Task | Frequency | Notes |
|------|-----------|-------|
| Verify USB‑C connection is secure | Monthly | Vibration in racks can loosen connectors |
| Measure 3.3V rail voltage | Quarterly | Should be 3.25–3.35V. Below 3.1V → PSU failing |
| Check PSU for overheating | Quarterly | PSU should be warm, not hot (> 60°C = problem) |
| Replace PSU | 3‑5 years | Electrolytic capacitors dry out |

---

## 🧹 Cleaning

| Component | Method | Frequency | Do NOT |
|-----------|--------|-----------|--------|
| Enclosure exterior | Damp cloth (water only) | Quarterly | Solvents, abrasive cleaners |
| Breadboard | Compressed air | Annually | Water, contact cleaners on live circuits |
| MQ‑2 module | Compressed air | Monthly | Water, vacuum (may damage heater) |
| SCT‑013 clamp | Dry cloth | Annually | Solvents on plastic housing |
| Board | Compressed air | Annually | Vacuum (static risk), water |

---

## 📝 Maintenance Log Template

```yaml
date: 2026-06-15
technician: <name>
tasks_completed:
  - Monthly smoke test: PASS
  - MQ-2 cleaning: DONE
  - Cable inspection: OK
notes: >
  DHT22 #1 reading 1.5°C high vs reference. Marked for replacement next quarter.
next_scheduled: 2026-07-15
```

Maintain a log in a shared location (Confluence, Notion, or a simple git repo) for audit trail.

---

## 🛑 End‑of‑Life / Decommissioning

| Component | Disposal Method | Notes |
|-----------|----------------|-------|
| LicheeRV Nano | WEEE recycling e‑waste | Remove microSD (wipe securely) |
| Sensors | WEEE recycling or reuse | DHT22/DS18B20/reed switches are reusable |
| SCT‑013 | WEEE recycling | Contains ferrite core — recyclable |
| Enclosure | Plastic recycling (#7 ABS — check local rules) | Labels may need removal |
| Cables | Copper recycling | Strip and recycle wire; recycle plastic insulation |
| Breadboard | Reuse or WEEE | Breadboards are almost infinitely reusable |

> **Before disposal:** Run `picclaw reset --factory` to wipe credentials and configuration.
