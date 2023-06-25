import subprocess
from subprocess import PIPE
clientIP = input("Please type in client public IP address: ")
keyName = input("Client key name(Location_key.pem): ")

p1 = subprocess.Popen(['sudo','apt', 'update'])
p1.wait()
p2 = subprocess.Popen(['wget', 'https://git.io/vpn', '-O', 'openvpn-ubuntu-install.sh'])
p2.wait()
p3 = subprocess.Popen('sudo chmod -v +x openvpn-ubuntu-install.sh', shell = True)
p3.wait()
p4 = subprocess.Popen('sudo ./openvpn-ubuntu-install.sh', shell=True)
p4.wait()
cmd = 'sudo scp -o StrictHostKeyChecking=no -i /home/ubuntu/'+keyName+' /root/client.ovpn ubuntu@'+clientIP+':/home/ubuntu'
p5 = subprocess.Popen(cmd, shell=True)
p5.wait()
if str(p5.returncode) == '1':
    print('Error: '+ p5.stderr)
else:
    print('Success! You can proceed on the target side!')









