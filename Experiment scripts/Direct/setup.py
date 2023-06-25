import subprocess
import os
p1 = subprocess.Popen('sudo apt update',shell=True)
p1.wait()
p2 = subprocess.Popen('sudo apt install -y python3-scapy',shell=True)
p2.wait()
p6 = subprocess.Popen('sudo apt-get install python3 python3-pip -y',shell=True)
p6.wait()
p7 = subprocess.Popen('sudo pip3 install pyshark',shell=True)
p7.wait()
p3 = subprocess.Popen('sudo apt-get install -y tshark',shell=True)
p3.wait()
p4 = subprocess.Popen('sudo apt-get install -y traceroute', shell = True)
p4.wait()
p5 = subprocess.Popen('sudo apt install -y curl', shell = True)
p5.wait()
p8 = subprocess.Popen('sudo mkdir /home/capture', shell = True)
p8.wait()

my_ip = os.popen('curl -s ifconfig.me').readline()
if my_ip == '129.7.241.21':
    filePath = '/home/tyuan/mycapture/target.py'
else:
    filePath = '/home/ubuntu/target.py'
print("Getting to target script.......")
p6 = subprocess.run(['sudo','python3',filePath])

if p6.returncode == 1:
    print('Error on target.py')
else:
    print('Collect-process finished! Check results')




