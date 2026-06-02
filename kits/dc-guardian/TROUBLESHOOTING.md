# 🔍 Troubleshooting Guide — DC Guardian

> Common edge‑case issues, diagnostics, and fixes.
> If you encounter a problem not listed here, [open an issue](https://github.com/Clawland-AI/clawland-kits/issues).

---

## 🚨 No Power / Board Won't Boot

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No LEDs on board, no serial output | USB‑C cable is power‑only (no data wires) | Use a **data‑capable** USB‑C cable |
| Board powers on but no PicClaw agent | microSD not flashed or corrupted | Re‑flash the microSD; try another card |
| Board crashes after 30 seconds | PSU < 2A under load | Use a **5V⎓2A minimum** PSU — phone chargers may be < 1.5A |
| Intermittent resets | Loose USB‑C connection | Secure cable; try cable with locking mechanism |

**Diagnostic flow:**
```
Board not responding?
  ├── Is USB‑C LED on? 
  │   ├── NO  → Try different cable/PSU
  │   └── YES → Check serial console at 115200 baud
  │              ├── No output → Re‑flash microSD
  │              └── Boots OK  → Check `picclaw status`
  └── picclaw status fails?
      └── PicClaw image may be corrupted → re‑flash
```

---

## 🌡️ DHT22 Reading 0°C or NaN Humidity

| Cause | Check | Fix |
|-------|-------|-----|
| Missing pull‑up resistor | Measure resistance between DATA and VCC | Add **10kΩ** from DATA to 3V3 |
| Cable too long (> 2m) | — | Shorten cable or use shielded twisted‑pair |
| Wrong pin assignment | Verify physical GPIO17/18 connection | Re‑wire to correct pin |
| Sensor damaged | Test sensor with Arduino/5V (DHT22 tolerates 5V) | Replace DHT22 |
| Timing issue | DHT22 needs strict ~18ms start pulse | Ensure PicClaw driver uses proper bit‑banging |

**Quick test:**
```bash
# Force a re-read
picclaw sensor read dht22_room
# Compare with a known‑good USB temp/humidity logger
```

---

## 🌡️ DS18B20 "Device Not Found"

| Cause | Check | Fix |
|-------|-------|-----|
| **Missing pull‑up resistor (most common!)** | Measure between DATA and 3V3 — should be ~4.7kΩ | Solder a **4.7kΩ resistor** between DATA (GPIO19) and 3V3 |
| Wrong wire colors | Probe wires vary by vendor | Use multimeter continuity to identify GND/VCC/DATA |
| 1‑Wire driver not loaded | `lsmod \| grep w1_gpio` | `modprobe w1_gpio` or add to `/etc/modules` |
| Parasitic power mode | DS18B20 can run in 2‑wire mode (VCC to GND) | Use 3‑wire mode: connect VCC to 3V3, not GND |
| Too many devices on bus | Each DS18B20 causes ~100µA pull‑down | Ensure only one device; remove extra pull‑downs |

**Verify with kernel:**
```bash
# Check if the 1-Wire bus sees the device
ls /sys/bus/w1/devices/
# → Should show 28-xxxxxxxxxxxx (DS18B20 ROM ID)
cat /sys/bus/w1/devices/28-xxxxxxxxxxxx/w1_slave
```

---

## 💧 Leak Probe False Positives

| Cause | Check | Fix |
|-------|-------|-----|
| Condensation | Probe on cold surface with high humidity | Elevate probe 1mm from surface; add thermal break |
| Electrical noise | Long unshielded cable > 3m | Use shielded twisted‑pair, ground shield at one end |
| GPIO floating (no input state defined) | GPIO20 configured? | Enable **internal pull‑DOWN** on GPIO20 in PicClaw config |
| Probe contamination | Residue from previous wet event | Clean with isopropyl alcohol; dry thoroughly |

**Diagnostic:**
```bash
# Read raw GPIO state
python -c "import gpiod; print(gpiod.Chip('gpiochip0').get_line(20).get_value())"
# → Should be 0 (dry). If 1 when dry → pull‑down missing.
```

---

## 🔥 MQ‑2 Smoke Sensor False Triggers

| Cause | Check | Fix |
|-------|-------|-----|
| Sensor warm‑up period | MQ‑2 needs **24–48 hours** burn‑in for stable readings | Run for 48h before setting thresholds |
| Sensitivity too high | Potentiometer on module | Turn potentiometer counter‑clockwise to raise threshold |
| Environmental vapors | Alcohol, cooking fumes, paint solvents | Relocate sensor away from non‑smoke vapor sources |
| Temperature/humidity drift | MQ‑2 sensitivity changes with ambient conditions | Allow 10°C±5°C and 60%±20% RH for stable baseline |

---

## 🚪 Reed Switch Not Detecting

| Cause | Check | Fix |
|-------|-------|-----|
| Magnet too far (> 5mm) | Measure gap distance | Reposition magnet within 5mm |
| Wrong GPIO polarity | Expects pull‑UP but configured as pull‑DOWN | Set **internal pull‑UP** on GPIO22/GPIO23 |
| NO vs NC confusion | Some reed switches are Normally Open, some Normally Closed | Verify with multimeter: closed when magnet near = NO |
| Wire too long (> 10m) | Voltage drop from thin wires | Use 22 AWG or thicker; keep runs < 10m |

---

## ⚡ SCT‑013 Current Reading Erratic

| Cause | Check | Fix |
|-------|-------|-----|
| Clamp around full cable bundle | Both L and N wires cancel each other | Clamp around **ONE** conductor only |
| ADC noise | ADS1115 near switching PSU | Move ADS1115 5cm+ from PSU; add 100nF cap on VDD |
| Wrong ADC range | ADS1115 default range is ±4.096V | Verify PicClaw ADC config matches ±4.096V |
| Missing burden resistor (SCT‑013‑000) | — | Add 33Ω burden resistor across signal and GND |
| 3.5mm jack oxidation | — | Unplug/replug; clean with contact cleaner |

---

## 📡 Network Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Board not reachable via SSH | — | Check serial console; `ip addr` to see IP assignment |
| mDNS hostname not resolving | Network doesn't support mDNS | Use static IP in `/etc/network/interfaces` |
| Alerts not sending | No internet connectivity | `ping 8.8.8.8`; check DNS: `nslookup api.telegram.org` |
| Webhook timeout | Endpoint unreachable from board network | Test with `curl -X POST https://your-webhook.com/test` |

---

## 🔇 Buzzer Not Sounding

| Cause | Check | Fix |
|-------|-------|-----|
| No transistor drive | GPIO24 → 1kΩ → Base(2N2222) wired? | Verify soldering; bypass transistor with direct GPIO→buzzer for quiet test |
| Polarity reversed | Active buzzer is polarized | Positive → transistor collector, Negative → GND |
| GPIO24 not set as output | Pin mode | `picclaw gpio mode GPIO24 out` |
| Buzzer needs > 3.3V | Some buzzers are 5V rated | Replace with 3.3V‑compatible buzzer |

---

## 🐧 Software / PicClaw Diagnostics

### Check PicClaw logs
```bash
journalctl -u picclaw --since "5 minutes ago"
# Or
picclaw logs --tail 50
```

### Check sensor configuration
```bash
picclaw sensor list
# → Should show all 7 configured sensors
picclaw sensor read dht22_room
```

### Check alert delivery
```bash
picclaw alert test --severity warning
# → Sends test alert to all configured channels
```

### Reset to factory
```bash
picclaw reset --factory
# ⚠️ This clears all skills, settings, and stored data
```

---

## 🧪 General Diagnostic Flow

```
Problem with a sensor?
  ├── Check physical wiring (pin map in WIRING.md)
  ├── Check power (3.3V at sensor VCC?)
  ├── Check GPIO voltage (3.3V at GPIO pin?)
  ├── Check I²C (i2cdetect for ADS1115)
  ├── Check driver/logs (picclaw sensor read)
  ├── Check network (alerts reachable?)
  └── Still stuck? 
      ├── Re‑read this guide
      ├── Check GitHub Issues for similar reports
      └── Open a new issue with `picclaw support bundle`
```

---

## 📞 Support Bundle Generation

```bash
# Generate a support bundle for issue reports
picclaw support bundle
# → Creates dc-guardian-support-YYYYMMDD-HHMMSS.tar.gz
# Includes: picclaw logs, sensor config, wiring pin map, network status
```
