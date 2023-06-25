# Experiment Steps

1. Create 3 AWS EC2 instances for client server, VPN server and target server. (3 AWS EC2 instances target server) (5 mins)
   - In security setting of VPN server, add a UDP inbound rule for port 1194 /0.0.0.0 (everything), and add ICMP inbound rule for all (this enables ping protocol for VPN).

2. Transfer files (5 mins)
   - Use filezilla to transfer “client” to "target.pem" client instance (make sure file path is /home/ubuntu) (sudo python3 VPN.py)
   - Use filezilla to transfer “VPN” and “client.pem” to VPN server. (This later will be used to distribute the “client.ovpn” file to client server using the “scp” protocol, and make sure the file path is /home/ubuntu)
   - Use filezilla to transfer “target” and “setup” to target server. (File path is /home/ubuntu for AWS)

3. Execute scripts (5 mins)
   - On VPN server, run “VPN” and follow user-input instructions. (Input “client” for file name when see the prompt)
   - On Target server, run “target” and follow the user-input instructions.
   - On Client server, run “client” and follow user-input instructions.
  
4. Collect files
   - On Target server, use filezilla to collect experiment result files in the path that is already mentioned above. (Default probing number: 5. Indicated by “Successfully collected +1 datapoint”)
