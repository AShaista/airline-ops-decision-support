# KPI to Data Mapping

This document maps each operational KPI to the corresponding columns
in the flight delay dataset.

The goal is to ensure transparency, consistency, and reproducibility
when computing metrics.

## Dataset Reference

**File**  
`data/raw/airline_delay_sample.csv`

Each row represents aggregated flight activity for a given:
- Airline
- Airport
- Time period (month / year)

## 1. On-Time Performance (OTP)

**KPI Definition**  
Percentage of flights that arrive within 15 minutes of scheduled arrival time.

**Dataset Columns Used**
- `arr_del15` (number of arrivals delayed more than 15 minutes)
- `arr_flights` (total arriving flights)

**Calculation Logic**
Flights arriving within 15 minutes =  
`arr_flights - arr_del15`

OTP =  
`(arr_flights - arr_del15) / arr_flights`

**Assumptions**
- Flights with arrival delay ≤ 15 minutes are considered on time
- Canceled and diverted flights are excluded from OTP

## 2. Average Arrival Delay (Minutes)

**KPI Definition**  
Average number of minutes flights arrive late.

**Dataset Columns Used**
- `arr_delay` (total arrival delay minutes)
- `arr_flights` (total arriving flights)

**Calculation Logic**
Average Arrival Delay =  
`arr_delay / arr_flights`

**Assumptions**
- Early arrivals reduce total delay minutes
- Aggregated delay minutes reflect average severity

## 3. Delay Rate (>15 Minutes)

**KPI Definition**  
Percentage of flights delayed more than 15 minutes.

**Dataset Columns Used**
- `arr_del15`
- `arr_flights`

**Calculation Logic**
Delay Rate =  
`arr_del15 / arr_flights`

**Assumptions**
- Threshold of 15 minutes aligns with industry OTP standards

## 4. Cancellation Rate

**KPI Definition**  
Percentage of scheduled flights that were canceled.

**Dataset Columns Used**
- `arr_cancelled`
- `arr_flights`

**Calculation Logic**
Cancellation Rate =  
`arr_cancelled / arr_flights`

**Assumptions**
- All cancellations are treated equally regardless of cause
- Diverted flights are not counted as cancellations

## 5. Delay Cause Distribution

**KPI Definition**  
Share of delay minutes by delay category.

**Dataset Columns Used**
- `carrier_delay`
- `weather_delay`
- `nas_delay`
- `security_delay`
- `late_aircraft_delay`

**Calculation Logic**
Delay Cause Share =  
`delay_category_minutes / total_delay_minutes`

**Assumptions**
- Delay causes are mutually exclusive
- Categories follow U.S. DOT definitions


## Notes and Limitations

- This dataset is aggregated and does not contain individual flight records
- Metrics are computed at an airline–airport–time-period level
- Results are intended for **trend analysis and decision support**, not regulatory reporting
