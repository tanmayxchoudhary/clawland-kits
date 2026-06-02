# ⚠️ Safety & Compliance — DC Guardian

> **Read this document BEFORE installing the DC Guardian in a production data center environment.**
> Non‑compliance with electrical safety codes can result in equipment damage, injury, or death.

---

## 🔌 Electrical Safety

### Mains Voltage Warning

**⚠️ The DC Guardian board and all sensor wiring operate at ≤ 3.3V DC (SELV — Safety Extra Low Voltage).**
**⚠️ The SCT‑013 current clamp senses mains current via induction — no galvanic connection to mains.**
**⚠️ Even so, the clamp must be installed on a live mains conductor. This must be done by a qualified person.**

```
┌─────────────────────────────────────────────────────────────┐
│                     SAFETY BOUNDARY                          │
│                                                              │
│   ╔══════════════╗     ╔══════════════╗     ╔══════════════╗│
│   ║   3.3V DC    ║     ║  Isolated    ║     ║   Mains AC   ║│
│   ║  (SELV)      ║ ←─→ ║  Sensor Gap  ║ ←─→ ║  (230/120V)  ║│
│   ║  Board+Sensor║     ║  (SCT-013)   ║     ║  (LIVE)      ║│
│   ╚══════════════╝     ╚══════════════╝     ╚══════════════╝│
│         ✓ Safe              ✓ Compliant        ✗ DANGER     │
│         to touch            with IEC 60950    Qualified     │
│                                              person only    │
└─────────────────────────────────────────────────────────────┘
```

### Rules for Electrical Safety

1. **Never** connect any sensor wire or GPIO pin to mains voltage.
2. **Never** work on live mains wiring — de‑energize the circuit before installing the SCT‑013.
3. **Never** clamp the SCT‑013 around a cable bundle — only **individual conductors**.
4. **Always** use strain relief where cables exit the enclosure.
5. **Always** label the enclosure: "DC GUARDIAN — LOW VOLTAGE EQUIPMENT — DO NOT OPEN WHILE ENERGIZED" if mounted near mains panels.
6. **Always** install the enclosure at least 1m away from mains distribution panels unless inside a dedicated low‑voltage cabinet.

---

## 🔥 Fire Safety

- The LicheeRV Nano board draws < 2W typical — it does not generate significant heat.
- The MQ‑2 sensor has a built‑in heater element that runs at ~150°C internally. The module body stays < 50°C. Ensure at least 2cm airflow clearance around the MQ‑2.
- Use the **vented** ABS enclosure (Hammond 1591 or similar) — never seal the board in an airtight box.
- If mounting in a combustible rack (wooden server racks), add a fire‑resistant barrier between the enclosure and the rack surface.

---

## 🧲 ESD (Electrostatic Discharge) Precautions

| Component | ESD Sensitivity | Handling Required? |
|-----------|:---------------:|--------------------|
| LicheeRV Nano | Moderate | Use grounded wrist strap when handling bare board |
| DHT22/DS18B20 | Low | Standard handling OK |
| ADS1115 | Moderate | Handle by edges, store in anti‑static bag |
| MQ‑2 | Low | Standard handling OK |

**General ESD handling:**
- Work on an **ESD‑safe mat** if possible
- Touch a grounded metal object before handling boards
- Store spare components in anti‑static bags

---

## 🏢 Data Center Compliance

### Rack Installation

| Requirement | Standard | Notes |
|-------------|----------|-------|
| Rack clearance | EIA‑310 | Fits in any 1U+ space; use blank panel adjacent |
| Airflow | ASHRAE TC 9.9 | Intake air < 27°C for reliable operation |
| Cable management | TIA‑606 | Label all cables per facility standard |
| Fire rating | UL 94 V‑0 | Enclosure material must be flame‑retardant |
| Grounding | TIA‑607 | Bond enclosure to rack ground if metal |

### Temperature Range

| Component | Operating Range | Notes |
|-----------|:---------------:|-------|
| LicheeRV Nano | 0°C to 70°C | Not rated for freezer/cold‑aisle containment |
| DHT22 | −40°C to 80°C | OK for all data center environments |
| DS18B20 | −55°C to 125°C | Wide range; ideal for cooling loop monitoring |
| MQ‑2 | −20°C to 50°C | **Limited** — not suitable for cold aisles below −20°C |
| SCT‑013 | −15°C to 60°C | Suitable for most data center environments |

---

## 📜 Regulatory Compliance Notes

| Regulation | Applicability | Status |
|-----------|--------------|--------|
| **IEC 60950‑1 / 62368‑1** | SELV circuits — board and sensor wiring | Compliant by design (≤ 3.3V) |
| **IEC 61010‑1** | Measurement equipment — SCT‑013 | Depends on clamp certification |
| **FCC Part 15** | Digital device emission limits | LicheeRV Nano may need shielded enclosure in regulated environments |
| **CE / UKCA** | EU/UK market | Board‑level components generally CE; full system certification is integrator responsibility |
| **RoHS** | Hazardous substance restriction | All listed components are RoHS‑compliant |
| **WEEE** | Waste electronics | Dispose of e‑waste at authorized recycling center |

> ⚠️ This kit is a **reference design** intended for evaluation and proof‑of‑concept use. Full regulatory certification for production deployment is the responsibility of the integrator.

---

## 🧰 Safe Work Practices

### Before Opening the Enclosure
1. Disconnect USB‑C power.
2. Wait 10 seconds for capacitors to discharge.
3. If SCT‑013 is installed, verify the mains circuit is de‑energized.

### In the Rack Room
1. Wear ESD‑safe footwear on conductive flooring.
2. Do not place the enclosure on top of UPS units or other heat sources.
3. Keep sensor cables away from sharp edges (use grommets in cable pass‑throughs).

---

## 🆘 Emergency Procedures

| Event | Immediate Action | Follow‑up |
|-------|-----------------|-----------|
| Smoke from enclosure | Disconnect USB‑C immediately. Unplug SCT‑013 clamp. | Inspect for overheating component. Replace enclosure. |
| Water on enclosure | Do NOT touch. Disconnect power at source. | Check leak alert threshold. Relocate enclosure. |
| Mains short near SCT‑013 | Call electrician. Do not approach. | Have SCT‑013 installation reviewed. |
| Burning smell from MQ‑2 | Normal for first 24h (sensor burn‑in). If persistent >48h, disconnect. | Replace MQ‑2 module. |

---

> **Last updated:** June 2026
> **Compliance review:** This document does not constitute legal or regulatory advice. Consult a qualified electrical engineer for production deployments.
