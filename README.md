# Research-Project-VPN-Detection
This is experimental pipeline design for real-time VPN traffic detection research project:
Repo consists of:
  1. Proof of concept
  2. Experimental scripts
  3. Protocol-level VPN/Non-VPN dataset 
  4. Preliminary study results

# Problem statement
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/5109ef96-d81e-4cc0-9b28-aa8d56c50e05)

Reasons to detect VPN traffic:
- Network security (anonymity network)
- Geolocation restrictions
- Content licensing

# Research landscape
Table of known VPN domains/IPs
- Incomplete coverage
- Resource-intensive

ISCXVPN2016 or time-related datasets
- Low generalizability
- Unsuitable for real-time use

Packet payload analysis
- Comparable challenges

# Motivations
- Existing datasets are often outdated or overly complex, missing new traffic patterns and VPN services.
- Existing methods struggle to create efficient, lightweight real-time VPN detection systems suitable for all application types, with optimal response times

# System Overview
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/a694302e-6cf9-4a8d-b2b6-532aae109eb6)

Primary attributes:
- RTT1
- RTT2
- Ratio of RTT2 over RTT1: RTT2/RTT1

# RTT1: Transport Layer Protocol
![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/f2dacd8d-1395-4188-a548-be287d3a04c2)

- RTT1 derives from the time interval between the ACK/SYN packet and the ACK packet during a TCP three-way handshake.
- A three-way handshake is a fundamental process used in computer networking to establish a connection between two devices. (TCP:HTTP/HTTPS, FTP, SFTP, SMTP, IMAP, POP3, Telnet, NNTP)(QUIC)(SCTP)(BGP)

# RTT2: Nearest Neighbors Approximation
- Attempted methods (failed)
  - SSH: lack prior knowledage of open destination port
  - PING: VPN's ICMP protocol can be disabled
  - TCP Reset Attack - A VPN transmits all types of packets without discrimination
- Traceroute (UNIX)
  - Traceroute identifies network paths and round-trip times by sending ICMP echo requests with increasing TTL values to the destination. Each router decreases the TTL; when it reaches zero, an ICMP Time Exceeded message returns to the source, revealing routers along the path.

  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/676fb916-fce8-45bf-8616-74c68096dad3)

- Algorithm Definition
  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/0e395446-d346-4a9f-92cf-ca1eb1db12f8)
  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/33bbbf3c-11fd-4a3e-a5d2-a5e0f09aa9a2)
  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/e092b25a-5794-46a8-a4a0-cc3dbbc09ecc)

  - RTT1: there way handshake
  - RTT2: Traceroute to the Nearest Neighbor (Approx.)
  
  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/38f32ebc-c159-45f0-9c55-79ee5ee19c92)
  ![image](https://github.com/yuantian94/Research-Project-VPN-Detection/assets/13746207/b4c08a15-b51f-4c3e-92d9-f7c334577e68)


