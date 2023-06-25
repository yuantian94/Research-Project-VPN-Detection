import sys
from datetime import datetime
import scapy
from scapy.all import *
import pyshark
import os
import time
import subprocess
import threading
import signal

packet_count = 0

def ping_capture():
    print('pinging......')
    s = 'timestamp '+ str(datetime.now())[:19]
    os.system('echo \"' + s + '\" >> '+shortPingPath)
    os.system('sudo ping -c 3 '+clientIP +' >> '+shortPingPath)
    os.system('echo \"------------------------------------------------------------------------------\" >> ' + shortPingPath)

def trace_capture():
    print('tracerouting....')
    s = 'timestamp ' + str(datetime.now())[:19]
    os.system('echo \"' + s + '\" >> '+shortTracePath)
    os.system('sudo traceroute -w0.6 -m50 -T -n ' + clientIP + ' >> '+shortTracePath)
    os.system(
        'echo \"------------------------------------------------------------------------------\" >> ' + shortTracePath)


def print_callback(pkt):
    try:
        global packet_count

        if pkt.tcp.seq == '1' and  pkt.tcp.ack == '1' and pkt.ip.src == clientIP and (pkt['tcp'].flags == '0x00000010' or pkt['tcp'].flags == '0x0010'):
            log = filename+','+clientIP+',ACK,'+pkt.ip.src+','+pkt.ip.dst+','+str(pkt.sniff_time)
            os.system('echo '+log+ ' >> '+longFilepath)
            os.system(
                'echo \"------------------------------------------------------------------------------\" >> ' + longFilepath)
            ping_thread = threading.Thread(target = ping_capture)
            ping_thread.start()
            trace_thread = threading.Thread(target = trace_capture)
            trace_thread.start()
            ping_thread.join()
            trace_thread.join()
            packet_count = packet_count+1
            print(packet_count)
            print("==========Successfully collected +1 datapoint============")
            if packet_count == 5:
                print("Closing in 5 secs")
                time.sleep(5)
                sys.exit()
        if pkt.tcp.ack == '1' and pkt.tcp.seq == '0' and pkt.ip.dst == clientIP and (pkt['tcp'].flags == '0x00000012' or pkt['tcp'].flags == '0x0012'):
            log = filename+','+clientIP+',SYN/ACK,'+pkt.ip.src+','+pkt.ip.dst+','+str(pkt.sniff_time)
            os.system('echo '+log+ ' >> '+longFilepath)
    except AttributeError as e:
        pass

def start():
    print("starting capture")
    try:
        capture_cmd1 = 'sudo tshark -i eth0 -w /home/capture/'+wireshark_filename
        process = subprocess.Popen(capture_cmd1, shell=True)
        capture.apply_on_packets(print_callback, timeout=100000)
    except:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        print("killing the process...")
        sys.exit()

if __name__ == "__main__":
    clientIP = input("Client Public IP address: ")
    filename = input("Location configuration(Client-Target): ")
    my_ip = os.popen('curl -s ifconfig.me').readline()
    
    wireshark_filename = filename + '_' + clientIP + '-' + my_ip + '.pcap'
    file_cmd1 = 'sudo touch /home/capture/'+ wireshark_filename
    file_cmd2 = 'sudo chmod 777 /home/capture/' + wireshark_filename
    p7 = subprocess.Popen(file_cmd1, shell=True)
    p7.wait()
    p8 = subprocess.Popen(file_cmd2, shell=True)
    p8.wait()
    interface = 'eth0'
    shortPingPath = '/home/ubuntu/' + filename + '-P.txt'
    shortTracePath = '/home/ubuntu/' + filename + '-T.txt'
    longFilepath = '/home/ubuntu/' + filename + '-L.txt'

    p1 = subprocess.Popen(['sudo', 'rm', shortPingPath])
    p1.wait()
    p2 = subprocess.Popen(['sudo', 'rm', longFilepath])
    p2.wait()
    p3 = subprocess.Popen(['sudo', 'rm', shortTracePath])
    p3.wait()
    p4 = subprocess.Popen(['sudo', 'touch', shortPingPath])
    p4.wait()
    p5 = subprocess.Popen(['sudo', 'touch', longFilepath])
    p5.wait()
    p6 = subprocess.Popen(['sudo', 'touch', shortTracePath])
    p6.wait()
    capture = pyshark.LiveCapture(interface=interface, bpf_filter='tcp port 22')
    start()
