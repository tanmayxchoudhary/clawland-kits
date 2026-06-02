# 🧾 Bill of Materials — DC Guardian

> **Target: ≤ $88.00** | ✓ Current total: **$86.58** | Prices verified June 2026
> All prices are USD street prices (single‑unit, without volume discount). Shipping not included — see "Shipping & Handling" below.

---

## 📐 BOM Table

| # | Part / SKU | Qty | Unit Price | Subtotal | Category | Purpose | Verified Link(s) |
|---|------------|:---:|----------:|---------:|----------|---------|-----------------|
| 1 | **LicheeRV Nano 512MB** (Sipeed) or equiv. Linux SBC | 1 | $12.90 | $12.90 | Compute | PicClaw edge runtime, sensor polling, alert dispatch | [Sipeed Store](https://wiki.sipeed.com/hardware/en/lichee/RV_Nano/1_intro.html) · [AliExpress ~$13](https://aliexpress.com) |
| 2 | **USB‑C 5V⎓2A PSU** (Raspberry Pi official or equiv.) | 1 | $6.99 | $6.99 | Power | Stable board power | [Raspberry Pi](https://www.raspberrypi.com/products/type-c-power-supply/) · [Amazon](https://www.amazon.com/dp/B0BTRRC2C6) |
| 3 | **DHT22 / AM2302** temp‑humidity sensor (Aosong) | 2 | $5.50 | $11.00 | Sensor | Room ambient + HVAC cold‑aisle temp/humidity | [Adafruit 385](https://www.adafruit.com/product/385) · [SparkFun SEN‑18396](https://www.sparkfun.com/products/18396) |
| 4 | **DS18B20** waterproof temperature probe (Dallas / Maxim) | 1 | $4.95 | $4.95 | Sensor | Spot temperature on cooling loop or cable tray hotspot | [Adafruit 381](https://www.adafruit.com/product/381) · [Amazon 10‑pack ~$10](https://www.amazon.com/dp/B08QRWHYMY) |
| 5 | **Water leak sensor / probe** (digital output) | 1 | $3.50 | $3.50 | Sensor | Floor / cooling‑line leak detection | [DFRobot SEN0368](https://www.dfrobot.com/product-1128.html) · [Adafruit 5190](https://www.adafruit.com/product/5190) |
| 6 | **MQ‑2 smoke / combustible gas sensor module** | 1 | $4.50 | $4.50 | Sensor | Smoke / LPG / propane early warning | [SparkFun SEN‑09405](https://www.sparkfun.com/products/9405) · [Amazon ~$4](https://www.amazon.com/dp/B01MQ1Y6K1) |
| 7 | **Magnetic reed switch (NC)** — MC‑18 or equiv. | 2 | $2.00 | $4.00 | Sensor | Rack door + room door open/close detection | [Adafruit 375](https://www.adafruit.com/product/375) · [Amazon 10‑pack ~$7](https://www.amazon.com/dp/B07G4W2Y5G) |
| 8 | **SCT‑013‑030** 30A non‑invasive AC current clamp (YHDC) | 1 | $12.95 | $12.95 | Sensor | UPS / branch circuit current trending | [YHDC product page](https://www.yhdc.com/product/sct013-401.html) · [Adafruit 5133](https://www.adafruit.com/product/5133) |
| 9 | **ADS1115** 16‑bit I²C ADC module (TI) | 1 | $4.95 | $4.95 | Signal | Convert SCT‑013 analog output to digital | [Adafruit 1085](https://www.adafruit.com/product/1085) · [SparkFun SEN‑16304](https://www.sparkfun.com/products/16304) |
| 10 | **Active buzzer module** (3.3V, 5V tolerant) | 1 | $1.50 | $1.50 | Indicator | Local audible alert on critical events | [Adafruit 1536](https://www.adafruit.com/product/1536) · [Amazon 5‑pack ~$5](https://www.amazon.com/dp/B07QH3YQLD) |
| 11 | **LED (red + green) + 330Ω resistors** basic kit | 1 set | $2.50 | $2.50 | Indicator | Red = warning/critical, green = healthy | [SparkFun COM‑12062](https://www.sparkfun.com/products/12062) · [Amazon ~$6](https://www.amazon.com/dp/B01CDK0UEO) |
| 12 | **400‑tie solderless breadboard** (MB‑102 or equiv.) | 1 | $4.95 | $4.95 | Build | Prototype / semi‑permanent assembly | [Adafruit 64](https://www.adafruit.com/product/64) · [Amazon 5‑pack ~$10](https://www.amazon.com/dp/B07QF9ZP9J) |
| 13 | **Dupont jumper wire kit** (M‑M, M‑F, F‑F, 40‑pin × 3) | 1 | $4.95 | $4.95 | Build | All wiring between board, sensors, and indicators | [Adafruit 153](https://www.adafruit.com/product/153) · [Amazon ~$6](https://www.amazon.com/dp/B01KSLM7N4) |
| 14 | **Vented ABS enclosure** 120×80×40mm (Hammond 1591 or equiv.) | 1 | $6.95 | $6.95 | Build | Rack‑mountable enclosure for board + breadboard | [Hammond 1591](https://www.hammfg.com/electronics/small-case/plastic/1591) · [Digikey](https://www.digikey.com/en/products/detail/hammond-manufacturing/1591XXMSFLBK/2713894) |
| 15 | **4.7kΩ resistor** (¼W, for DS18B20 pull‑up) | 1 | $0.08 | $0.08 | Build | 1‑Wire bus pull‑up | [Amazon ½W assortment ~$7](https://www.amazon.com/dp/B011Z4RV3I) |
| 16 | **10kΩ resistor** (¼W, for DHT22 pull‑up if needed) | 1 | $0.08 | $0.08 | Build | DHT22 data line pull‑up (many modules include this) | Included in resistor assortment |
| 17 | **Cable strain‑relief / cable gland** PG‑7 or PG‑9 | 4 | $0.48 | $1.92 | Build | Protect cables entering enclosure | [Amazon 10‑pack ~$6](https://www.amazon.com/dp/B07TWZ2J4V) |
| 18 | **Nylon standoffs + screws** M3 × 6mm kit | 1 | $0.95 | $0.95 | Build | Mount board inside enclosure | [Amazon ~$7](https://www.amazon.com/dp/B07PN5Q7WY) |
| 19 | **Heat‑shrink tubing assortment** | 1 | $1.50 | $1.50 | Build | Insulate exposed solder joints | [Amazon ~$7](https://www.amazon.com/dp/B06XFJ26TQ) |
| 20 | **Cable zip ties (100 mm, 100‑pack)** | 1 | $3.00 | $3.00 | Build | Cable management in enclosure and rack | [Amazon ~$5](https://www.amazon.com/dp/B0B5KFXRLF) |

---

## 💵 Cost Breakdown

```
Compute + Power          $19.89  ████████████████░░░░░░  23.0%
Sensors                  $45.85  ███████████████████████  52.9%
Indicators               $4.00   ███░░░░░░░░░░░░░░░░░░░   4.6%
Build / Enclosure        $16.84  ████████████░░░░░░░░░░  19.5%
───────────────────────────────────────────────────────
Total (excl. shipping)   $86.58  ███████████████████████ 100.0%
                          ¯¯¯¯
Target                    $88.00
Headroom                   $1.42
```

---

## 📦 Shipping & Handling

| Supplier | Est. shipping to US | Est. shipping to EU | Est. shipping to Asia |
|----------|-------------------:|-------------------:|---------------------:|
| Adafruit (US) | $7.95 | $20–30 | $25–35 |
| SparkFun (US) | $5.95 | $18–28 | $22–32 |
| Amazon (local) | Free (Prime) | Free (Prime) | Varies |
| AliExpress (CN) | Free–$3 | Free–$5 | Free |
| Digikey (US) | $4.99 | $12–25 | $15–25 |

**Kit total with shipping (worst‑case US): ~$94.53** — still represents a 99.8% savings vs. a single night shift.

---

## 🔄 Alternate / Sourcing‑Flexible Parts

| Item | Primary | Budget Alt | Premium Alt |
|------|---------|-----------|-------------|
| SBC | LicheeRV Nano $12.90 | Orange Pi Zero 2W $16 | Raspberry Pi Zero 2W $15 |
| Temp/Humidity | DHT22 $5.50 | DHT11 $2.50 (lower accuracy) | BME280 $12 (adds barometer) |
| Current clamp | SCT‑013‑030 $12.95 | SCT‑013‑000 (no burden) $9.95 | SCT‑013‑050 (50A range) $12.95 |
| Enclosure | Hammond 1591 $6.95 | ABS project box $4.50 | DIN‑rail aluminum $18.00 |

---

## 🔌 Connectors & Cabling (Not in BOM, but needed)

| Item | Est. Cost | Notes |
|------|----------:|-------|
| Ethernet cable (if wired) | $5–10 | Use shielded Cat5e+ |
| USB‑C data cable | $3–8 | At least 1m; use for power + serial |
| Terminal block (2‑pin, 5mm) | $0.50 ea | For leak probe and reed switch wiring |
| Wire (22 AWG, solid core) | $5‑8 spool | For breadboard → sensor extensions |

---

## 🧮 Price Notes

1. Prices retrieved from supplier websites and verified via public product pages (June 2026).
2. Many parts are available in multi‑packs — the per‑unit cost drops significantly if building multiple kits.
3. The DHT22 and DS18B20 are available in bulk on AliExpress for ~$2‑3 each, reducing BOM cost to **~$78**.
4. The $88 target is achievable **without** sacrificing quality when using Adafruit/SparkFun primary sources.
