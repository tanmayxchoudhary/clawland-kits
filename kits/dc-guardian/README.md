# 🛡️ DC Guardian Kit

**Edge-monitoring kit for unattended data-center night shifts.** Replace a $48,000/yr human operator with an ~$88 one-time hardware kit + $30/yr maintenance.

---

## 📋 What It Monitors

| Sensor | Target | Purpose |
|--------|--------|---------|
| DHT22 × 2 | Rack exhaust + HVAC cold aisle | Ambient temperature and humidity trends |
| DS18B20 (waterproof) | Cooling loop surface or cable tray | Spot temperature near failure points |
| Water leak probe | Floor drain / cooling pipe base | Early flood detection |
| MQ‑2 gas/smoke module | Rack air intake | Smoke / combustible gas early warning |
| Reed switch × 2 | Rack door + room door | Unauthorized / unattended door events |
| SCT‑013 + ADS1115 | UPS or branch circuit conductor | Non‑invasive current trend monitoring |

---

## 📦 Deliverables

| File | Description |
|------|-------------|
| [BOM.md](BOM.md) | Full parts list with verified SKUs, pricing tiers, and alternate suppliers |
| [WIRING.md](WIRING.md) | Pin map, Mermaid wiring diagram, Fritzing‑style breadboard layout |
| [ASSEMBLY.md](ASSEMBLY.md) | Step‑by‑step build with bench test, calibration, and installation |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Edge‑case diagnostics, common faults, and signal‑integrity guide |
| [SAFETY.md](SAFETY.md) | Electrical safety, NEC compliance, rack installation best practices |
| [MAINTENANCE.md](MAINTENANCE.md) | Periodic checks, sensor recalibration schedule, lifecycle planning |
| [skill.yaml](skill.yaml) | PicClaw scenario configuration |
| [alerts.yaml](alerts.yaml) | Alert thresholds, notification channels, escalation rules |
| [drivers/](drivers/) | Lightweight sensor readers (DHT22, DS18B20, discrete, SCT‑013) |

---

## 💰 ROI Calculation

| Cost Item | Amount |
|-----------|-------:|
| Human night‑shift operator (annual) | $48,000.00 |
| DC Guardian hardware (one‑time) | $86.58 |
| Maintenance reserve (annual) | $30.00 |
| **First‑year net savings** | **$47,883.42** |
| **Payback period** | **< 1 shift** |

> ROI assumes 24/7 coverage — replacing a single full‑time night‑shift operator with the kit's continuous, always‑alert monitoring.

---

## ⚡ Quick Start

```bash
# 1. Order parts from BOM.md
# 2. Wire per WIRING.md
# 3. Flash PicClaw onto LicheeRV Nano
picclaw image write --board licheerv-nano

# 4. Install the skill
picclaw skill install ./kits/dc-guardian

# 5. Verify
picclaw status
picclaw gateway
# → healthz endpoint responds 200
```

---

## ⚠️ Important

- This kit uses **isolated current sensors only** — no mains‑voltage connections to the board.
- Have any mains‑clamp installation reviewed by a qualified electrician.
- Read [SAFETY.md](SAFETY.md) before installing in production.
