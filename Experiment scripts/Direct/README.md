# Experiment Steps

1. Create 2 AWS EC2 instances for client server, VPN server and target server. (2 AWS EC2 instances target server) (5 mins)


2. Transfer files (5 mins)
   - Use filezilla to transfer “client” and “target.pem” to client instance (make sure file path is /home/ubuntu)
   - Use filezilla to transfer “target” and “setup” to target server. (File path is /home/ubuntu for AWS)

3. Execute scripts (5 mins)
   - On Target server, run “target” and follow the user-input instructions.
   - On Client server, run “client” and follow user-input instructions.
  
4. Collect files
   - On Target server, use filezilla to collect experiment result files in the path that is already mentioned above. (Default probing number: 5. Indicated by “Successfully collected +1 datapoint”)
