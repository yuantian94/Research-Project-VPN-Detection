import subprocess
import time
import threading
import os

commands = [
            "ls -l",
            "mkdir test",
            "cd test",
            "touch test.txt",
            "echo \"hello, world!\" >> test.txt",
            "cat test.txt",
            "rm test.txt",
            "cd ..",
            "rm -r test",
            "exit"
            ]

def ssh():
    time.sleep(10)
    for x in range(5):
        start_time = time.time()
        print('SSHing.....')
        p5 = subprocess.Popen(["sudo",
                               "ssh",
                               "-i",
                               f"/home/ubuntu/{keyName}",
                               "-o",
                               "StrictHostKeyChecking=no",
                               "-o",
                               "BatchMode=yes",
                               f"ubuntu@{targetIP}",
                               "&&".join(commands)
                               ])
        p5.wait()
        if x != 4:
            time.sleep(30)




targetIP = input("Target server IP address: ")
targetLocation = input("Target Location for key: ")
keyName = targetLocation+".pem"
p1 = subprocess.Popen(['sudo','apt', 'update', '-y'])
p1.wait()
p2 = subprocess.Popen(['sudo','apt', 'install', 'openvpn','-y'])
p2.wait()
p3 = subprocess.Popen('sudo cp /home/ubuntu/client.ovpn /etc/openvpn/client.conf', shell = True)
p3.wait()
ssh_thread = threading.Thread(target = ssh)
ssh_thread.start()
p4 = subprocess.Popen('sudo openvpn --client --config /etc/openvpn/client.conf', shell=True)




