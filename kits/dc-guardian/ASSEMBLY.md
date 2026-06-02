# 🔧 Assembly Instructions — DC Guardian

> **Estimated build time:** 45–75 minutes (bench) + 30 minutes (rack installation)
> **Skill level:** Intermediate — basic soldering, crimping, and multimeter use required

---

## 🧰 Tools Required

| Tool | Purpose | Alternative |
|------|---------|-------------|
| Wire cutter/stripper (22–26 AWG) | Trimming and stripping sensor wires | Scissors + sandpaper |
| Small flat‑head screwdriver (#00) | Terminal block screws | Precision set |
| Digital multimeter | Continuity check, voltage verification, sensor test | Any cheap DMM |
| Soldering iron (25W+) + solder | Resistor lead soldering, transistor wiring | Breadboard‑compatible alternatives |
| Heat‑gun or lighter | Heat‑shrink tubing on soldered joints | Electrical tape (temporary) |
| Laptop with USB‑C | PicClaw flashing, serial console, SSH | Any computer with USB |
| Label maker / fine‑tip marker | Cable labeling | Masking tape + pen |
| Crimping tool (optional) | Dupont terminal crimping | Pre‑crimped jumper wires |
| Helping hands (optional) | Soldering assistance | Vice + patience |

---

## 📦 Unboxing & Parts Check

Before starting, verify you have all 14 core BOM items. Lay everything out and check:

```
☐ LicheeRV Nano board
☐ USB‑C PSU (5V⎓2A min)
☐ DHT22 sensors × 2
☐ DS18B20 probe × 1
☐ Water leak probe × 1
☐ MQ‑2 module × 1
☐ Reed switches × 2
☐ SCT‑013‑030 × 1
☐ ADS1115 module × 1
☐ Active buzzer × 1
☐ Red + green LED + 330Ω resistors
☐ 400‑tie breadboard
☐ Dupont jumper wire kit
☐ Vented ABS enclosure
☐ 4.7kΩ resistor (DS18B20 pull‑up)
☐ 10kΩ resistor (DHT22 pull‑up, backup)
☐ Cable glands × 4
☐ Standoffs, heat‑shrink, zip ties
```

<!-- PHOTO: Unboxed parts laid out on workbench with labels -->

---

## 📐 Step 1 — Bench‑Check the Board

**Goal:** Verify the LicheeRV Nano boots and runs PicClaw.

### 1.1 Flash PicClaw (if not pre‑loaded)
```bash
# Download the PicClaw image for LicheeRV Nano
wget https://picclaw.io/releases/latest/picclaw-licheerv-nano.img.xz

# Write to microSD (assuming /dev/sdX on your laptop)
xzcat picclaw-licheerv-nano.img.xz | sudo dd of=/dev/sdX bs=4M status=progress
sync
```

### 1.2 First boot
1. Insert microSD card into LicheeRV Nano.
2. Connect USB‑C cable (data+power) to laptop or PSU.
3. Wait 30–60 seconds for boot.
4. Find the board on the network:
   ```bash
   # Option A: Serial console (115200 baud)
   screen /dev/ttyUSB0 115200

   # Option B: mDNS
   ping picclaw-xxxxxxxx.local

   # Option C: Check router DHCP assignments
   ```

### 1.3 Verify PicClaw
```bash
picclaw status
# → Should show: agent=picclaw, version=X.Y.Z, uptime=N seconds

picclaw gateway
# → Should start the HTTP gateway on port 8080

curl http://picclaw-xxxxxxxx.local:8080/healthz
# → {"status":"ok","agent":"picclaw"}
```

> ✅ **Photo checkpoint:** Board powered on, serial console or SSH visible with `picclaw status` output.

---

## 🔌 Step 2 — Wire the Power Rails

**Goal:** Build a reliable power distribution network on the breadboard.

1. Insert the LicheeRV Nano into the breadboard (or connect via Dupont wires — recommended for prototyping).
2. Run a **red (3V3)** wire from board pin 1 to the breadboard **red (+) power rail**.
3. Run a **black (GND)** wire from board pin 39 to the breadboard **blue (−) ground rail**.
4. **Prove the rails:** Use your multimeter in continuity mode between red rail and blue rail — should read **open** (infinite). Then power on briefly and measure **3.25–3.35V** between the rails.
5. Power off before connecting any sensors.

> ⚠️ **Never connect or disconnect sensors while the board is powered.** Always disconnect USB‑C first.

> ✅ **Photo checkpoint:** Breadboard with only power rails wired, DMM showing 3.3V.

---

## 🔬 Step 3 — Wire I²C Bus (ADS1115)

The ADS1115 is the gateway for the SCT‑013 current clamp.

1. Insert ADS1115 across the breadboard center gap.
2. Wire:
   - **VDD** → 3V3 rail
   - **GND** → GND rail
   - **SCL** → GPIO3 (pin 5 on board)
   - **SDA** → GPIO2 (pin 3 on board)
   - **ADDR** → GND (address 0x48)
3. Power on and scan the I²C bus:
   ```bash
   i2cdetect -y 0
   # → Should show device at 0x48
   ```

> ⚠️ I²C pull‑up resistors (10kΩ) are usually built into the ADS1115 module. If you see flickering addresses, add external 10kΩ pull‑ups from SCL→3V3 and SDA→3V3.

> ✅ **Photo checkpoint:** ADS1115 wired, `i2cdetect` output showing 0x48.

---

## 🌡️ Step 4 — Wire DHT22 Sensors

**Two sensors — label them before wiring!**

### DHT22 #1 (Room / rack exhaust)
| Pin | Connect to |
|-----|-----------|
| VCC (pin 1) | 3V3 rail |
| DATA (pin 2) | GPIO17 |
| GND (pin 4) | GND rail |

### DHT22 #2 (HVAC / cold aisle)
| Pin | Connect to |
|-----|-----------|
| VCC (pin 1) | 3V3 rail |
| DATA (pin 2) | GPIO18 |
| GND (pin 4) | GND rail |

### Pull‑up check
Some DHT22 modules include a built‑in pull‑up resistor. Check by measuring resistance between DATA and VCC — if you see ~10kΩ, you're good. If open, add a 10kΩ resistor between DATA and 3V3.

### Smoke test
```bash
python drivers/read_dht22.py --pin GPIO17 --name room
python drivers/read_dht22.py --pin GPIO18 --name hvac
```

**Expected:**
```json
{"ok": true, "pin": "GPIO17", "name": "room", "temperature_c": 24.8, "humidity_percent": 45.2}
```

> ⚠️ DHT22 can report 0% humidity or NaN if DATA line is improperly pulled up or cable is too long.

> ✅ **Photo checkpoint:** Both DHT22 wired, terminal showing JSON output from each.

---

## 🌡️ Step 5 — Wire DS18B20 Probe

**CRITICAL:** The DS18B20 requires a 4.7kΩ pull‑up on the data line. Without it, the sensor will not respond.

1. Wire the waterproof probe:
   - **Red** → 3V3 rail
   - **Yellow (DATA)** → GPIO19
   - **Black** → GND rail
2. Solder a **4.7kΩ resistor** between GPIO19 (DATA) and 3V3.
3. Cover the resistor leads with heat‑shrink.

### Verify pull‑up
Measure resistance between GPIO19 and 3V3 — should read **4.7kΩ ± 5%**.

### Smoke test
```bash
python drivers/read_ds18b20.py --pin GPIO19
```
**Expected:**
```json
{"ok": true, "pin": "GPIO19", "temperature_c": 23.6}
```

> ⚠️ If you get `{"ok": false, "error": "device not found"}`, check:
> - Pull‑up resistor value (4.7kΩ ± 1%, not 10kΩ)
> - Wiring — red/black/yellow may vary by vendor
> - 1‑Wire bus often needs the GPIO configured as `open_drain` with kernel `w1‑gpio` driver

> ✅ **Photo checkpoint:** DS18B20 probe wired with visible pull‑up resistor, terminal output.

---

## 🔔 Step 6 — Wire Discrete Sensors

### MQ‑2 Smoke/Gas Module
| Pin | Connect to |
|-----|-----------|
| VCC | 3V3 rail |
| GND | GND rail |
| DO | GPIO21 |
| AO | *Leave unconnected* |

The MQ‑2 module has a comparator (LM393) that drives DO HIGH when gas exceeds the potentiometer‑set threshold. The AO pin outputs raw analog voltage from the sensing element — it's unused in this configuration.

> 🔧 **Calibration:** In clean air, adjust the on‑board potentiometer so the DO LED just turns off. This sets the trip threshold.

### Water Leak Probe
| Pin | Connect to |
|-----|-----------|
| VCC | 3V3 rail |
| GND | GND rail |
| DO | GPIO20 |

Most leak probes output **HIGH** (3.3V) when moisture is detected and **LOW** when dry.

### Reed Switches × 2
Reed switches are polarity‑agnostic (passive devices). Connect:
- **One leg** → GPIO22 (#1) or GPIO23 (#2)
- **Other leg** → GND

Configure PicClaw to enable **internal pull‑UP** on these GPIOs. When the magnet is near (door closed), the switch shorts to GND → GPIO reads LOW. When the door opens, the switch opens → pull‑up pulls GPIO HIGH.

### Smoke test for discrete sensors
```bash
python drivers/read_discrete.py --pin GPIO20 --name leak
python drivers/read_discrete.py --pin GPIO21 --name smoke
python drivers/read_discrete.py --pin GPIO22 --name door_rack
python drivers/read_discrete.py --pin GPIO23 --name door_room
```
**Expected:**
```json
{"ok": true, "pin": "GPIO20", "name": "leak", "active": false}
```

> ✅ **Photo checkpoint:** All discrete sensors wired, terminal showing all four sensor JSON outputs.

---

## 🔊 Step 7 — Wire Indicators

### Buzzer (via NPN transistor)
GPIO24 cannot source enough current for a loud buzzer. Use a 2N2222 transistor:

```
GPIO24 ──┬─ 1kΩ ── Base (2N2222)
         │
         └───────── Emitter → GND
                   Collector → Buzzer(−)
                   Buzzer(+) → 3V3
```

This configuration lets the buzzer draw up to 200 mA from the 3V3 rail directly, controlled by GPIO24.

### Red LED
```
GPIO25 ──┬─ 330Ω ── Red LED (Anode)
         │                 (Cathode) → GND
```

### Green LED
```
GPIO26 ──┬─ 330Ω ── Green LED (Anode)
         │                   (Cathode) → GND
```

### Smoke test
```bash
# Test buzzer
picclaw gpio set GPIO24 high   # Buzzer ON
sleep 1
picclaw gpio set GPIO24 low    # Buzzer OFF

# Test LEDs
picclaw gpio set GPIO25 high   # Red ON
picclaw gpio set GPIO26 high   # Green ON
```

> ✅ **Photo checkpoint:** LEDs lit, buzzer audible.

---

## ⚡ Step 8 — Wire SCT‑013 Current Clamp

**⚠️ SAFETY FIRST:** The SCT‑013 clamp must be installed by a qualified person if used on mains wiring.

1. Plug the SCT‑013 3.5mm jack into the ADS1115:
   - **Jack tip (signal)** → ADS1115 A0
   - **Jack sleeve (GND)** → ADS1115 GND (or breadboard GND)
2. **Do NOT** add burden resistors — the SCT‑013‑030 has an internal burden resistor.

### Test with a known load
```bash
# With the clamp around nothing (zero current)
python drivers/read_sct013.py
# → {"ok": true, "current_A": 0.0, "raw_adc": 16384}

# Clamp around a powered device, then re-run
python drivers/read_sct013.py
# → {"ok": true, "current_A": 1.2, "raw_adc": 17200}
```

### Calibration constant
The SCT‑013‑030 outputs 1V at 30A. With the ADS1115 at ±4.096V range (default), the conversion is:
```
Current (A) = (adc_reading - 16384) * (30.0 / 8192)
```

This formula is pre‑configured in the driver.

> ✅ **Photo checkpoint:** SCT‑013 clamped around a device, terminal output showing non‑zero current.

---

## 🏗️ Step 9 — Load the Scenario Config

```bash
# From the repo root
picclaw skill install ./kits/dc-guardian

# Verify
picclaw skill list
# → dc-guardian (version 1.0.0) should be listed

# Start the gateway
picclaw gateway
```

### Test each alert path (acceptance test)

| Test | Method | Expected Alert | Expected LED |
|------|--------|---------------|-------------|
| **High temp** | Warm DHT22 #1 gently with your hand | Warning alert via Telegram/Discord/webhook | Red LED ON |
| **Leak** | Bridge leak probe with a wet cloth | Critical leak alert | Red LED ON, buzzer sounds |
| **Smoke** | Press MQ‑2 module test button (if available) | Critical smoke alert | Red LED ON, buzzer sounds |
| **Door open** | Move magnet away from reed switch | Security alert (door open 60s → warning) | Red LED ON |
| **Current** | Clamp around a known load | Non‑zero current sample logged | Green LED ON |

---

## 🏭 Step 10 — Install in the Rack Room

1. **Power down** and disconnect all USB cables.
2. **Prepare the enclosure:**
   - Drill holes for cable glands (PG‑7: 12mm drill bit)
   - Mount board on standoffs inside the enclosure
   - Thread all sensor cables through glands
3. **Route cables** with strain relief — label each:
   ```
   ┌─────────────────────────────────────┐
   │  DHT22_ROOM    ──── Cable gland #1  │
   │  DHT22_HVAC    ──── Cable gland #2  │
   │  DS18B20       ──── Together w/ #2  │
   │  LEAK_PROBE    ──── Cable gland #3  │
   │  REED_RACK     ──── Together w/ #3  │
   │  REED_ROOM     ──── Together w/ #3  │
   │  SCT013        ──── Cable gland #4  │
   └─────────────────────────────────────┘
   ```
4. **Place sensors** per the [placement rules in WIRING.md](WIRING.md#-installation-placement-rules).
5. **Secure** all cables with zip ties inside and outside the enclosure.
6. **Label** the enclosure: "DC GUARDIAN — DATA CENTER MONITOR"
7. **Restore power** — confirm board boots and gateway starts.
8. **Verify alerts** — trigger each test again to confirm alerts reach Telegram/Discord.

> ✅ **Photo checkpoint:** Final enclosed unit, mounted sensors in place, cable labeling visible, dashboard/alert screenshot.

---

## ✅ Acceptance Test Checklist

```
☐ DHT22 #1 reports ±0.5°C of reference thermometer
☐ DHT22 #2 reports ±0.5°C of reference thermometer  
☐ DS18B20 reports within ±0.5°C of DHT22 at same location
☐ Leak probe triggers alert when wet
☐ MQ‑2 smoke test triggers critical alert
☐ Reed switches register door state changes
☐ SCT‑013 current reading within ±5% of reference clamp meter
☐ Buzzer sounds on critical alerts
☐ Red LED illuminates on warning/critical
☐ Green LED illuminates when all sensors normal
☐ Alerts reach Telegram within 10 seconds
☐ Alerts reach Discord within 10 seconds
☐ Webhook endpoint receives POST on alert
☐ All cables labeled
☐ Enclosure closed and secured
☐ Unit installed in rack
```
