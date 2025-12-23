
# Airline Operations KPI Definitions

This document defines the key performance indicators (KPIs) used in the
Airline Operations Decision Support System.
All KPIs are designed to support operational decision-making and on-time
performance improvement.

## 1. On-Time Performance (OTP)

**Definition**  
Percentage of flights that arrive within 15 minutes of the scheduled arrival time.

**Formula**  
OTP = (Number of flights with arrival delay ≤ 15 minutes) / (Total completed flights)

**Why it matters**  
OTP is the primary industry metric for measuring airline operational reliability
and customer experience.

## 2. Average Arrival Delay (Minutes)

**Definition**  
Average number of minutes flights arrive late or early relative to the scheduled arrival time.

**Formula**  
Average Arrival Delay = Mean(arrival delay in minutes)

**Why it matters**  
Provides insight into the severity of delays beyond the OTP threshold.


## 3. Average Departure Delay (Minutes)

**Definition**  
Average number of minutes flights depart late or early relative to the scheduled departure time.

**Formula**  
Average Departure Delay = Mean(departure delay in minutes)

**Why it matters**  
Helps identify upstream operational issues such as gate congestion, crew readiness,
or late incoming aircraft.


## 4. Delay Rate (>15 Minutes)

**Definition**  
Percentage of flights with arrival delays greater than 15 minutes.

**Formula**  
Delay Rate = (Number of flights with arrival delay > 15 minutes) / (Total completed flights)

**Why it matters**  
Complements OTP by focusing specifically on delayed flights.

## 5. Cancellation Rate

**Definition**  
Percentage of scheduled flights that were canceled.

**Formula**  
Cancellation Rate = (Number of canceled flights) / (Total scheduled flights)

**Why it matters**  
Cancellations represent severe operational disruptions and have high customer impact.


## 6. Delay Cause Distribution

**Definition**  
Breakdown of delay minutes by cause category (e.g., weather, late aircraft, NAS, security).

**Why it matters**  
Helps operations teams prioritize interventions by identifying the most common
sources of disruption.
