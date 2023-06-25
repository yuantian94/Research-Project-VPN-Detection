# Research-Project-VPN-Detection
This is experimental pipeline design for real-time VPN traffic detection research project:
Repo consists of:
  1. Proof of concept
  2. Experimental scripts
  3. Protocol-level VPN/Non-VPN dataset 
  4. Preliminary study results

# Problem statement
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/6a734e35-09f0-4085-a410-da6b43cab077)

# Research landscape
Table of known VPN domains/IPs
  1. Incomplete coverage
  2. Resource-intensive

ISCXVPN2016 or time-related datasets
  1. Low generalizability
  2. Unsuitable for real-time use

Packet payload analysis
  1. Comparable challenges

# Motivations
1. Existing datasets are often outdated or overly complex, missing new traffic patterns and VPN services.
2. Existing methods struggle to create efficient, lightweight real-time VPN detection systems suitable for all application types, with optimal response times

# System Overview
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/a694302e-6cf9-4a8d-b2b6-532aae109eb6)
Primary attributes:
- RTT1
- RTT2
- Ratio of RTT2 over RTT1: RTT2/RTT1

# RTT1: Transport Layer Protocol
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/77074c7f-dcf2-4493-b7ec-57b751946819)
