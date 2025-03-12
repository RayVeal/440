""" Ramon Veal
cmsc 440
fall 2023 
programming assignment 2"""

import socket
import sys
import time
import random


""" ping header should be printed as:
    
o ---------- Ping Packet Header ----------
o Version: <Version field>
o Sequence No.: <SequenceNo field>
o Time: <Timestamp field>
o Payload Size: <Size field>
o --------- Ping Packet Payload ----------
o Host: <hostname>
o Class-name: VCU-CMSC440-FALL-2023
o User-name: <your last name>, <your first name>
o ------------------------------------------------ """


""" construct and send a valid PING packet consisting of a PING
header and PING payload """

def pack_packet(seq_no, hostname, version=1):
    timestamp = time.time()
    payload = f"Host: {hostname}\nClass-name: VCU-CMSC440-FALL-2023\nUser-name: Veal, Ramon"
    size = len(payload)
    
    header = f"---------- Ping Packet Header ----------\nVersion: {version}\nSequence No.: {seq_no}\nTime: {timestamp}\nPayload Size: {size}\n"
    payload_section = "--------- Ping Packet Payload ----------\n" + payload + "\n------------------------------------------------"
    
    return header + payload_section


""" parse the received reply packet """

def pack_reply_packet(seq_no, timestamp, size, hostname, version=1):
    payload = f"Host: {hostname.upper()}\nClass-name: VCU-CMSC440-FALL-2023\nUser-name: Veal, Ramon"
    
    header = f"----------- Ping Reply Header -----------\nVersion: {version}\nSequence No.: {seq_no}\nTime: {timestamp}\nPayload Size: {size}\n"
    payload_section = "----------- Ping Reply Payload -----------\n" + payload + "\n------------------------------------------"
    
    return header + payload_section


"""  client accepts two command-line arguments: the first one is either
the hostname or the IP of your ping server, and the second is the port number
your server is running at. 

send 10 pings to the server. first tries to
receive a response from the server for the ping packet it just sent before sending
the next packet. 

wait for up to 1 second for a reply; if no reply is received within 1
second, assume that the packet was lost during
transmission across the network and transmit the next packet"""

def ping_client(hostname, port, num_pings=10):
    server_address = (hostname, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)  # Set socket timeout to 1 second
    
    min_rtt = float('inf')
    max_rtt = 0
    total_rtt = 0
    packets_received = 0
    
    """  ping client sends ping packets to the ping server given in the
hostname/IP and the port through a UDP connection. """
    
    try:
        for seq_no in range(1, num_pings + 1):
            ping_packet = pack_packet(seq_no, hostname)
            print(ping_packet)
            
            try:
                start_time = time.time()
                sock.sendto(ping_packet.encode(), server_address)
                
                data, addr = sock.recvfrom(1024)
                end_time = time.time()
                
                reply_packet = data.decode()
                print(reply_packet)
                
                rtt = (end_time - start_time) * 1000  # Convert to milliseconds
                print(f"Round-Trip Time (RTT): {rtt:.3f} ms\n")
                
                min_rtt = min(min_rtt, rtt)
                max_rtt = max(max_rtt, rtt)
                total_rtt += rtt
                packets_received += 1
                
            except socket.timeout:
                print("----------- Ping Reply Timed Out -----------\n")
    
    finally:
        sock.close()
    
    if packets_received > 0:
        avg_rtt = total_rtt / packets_received
        packet_loss_rate = ((num_pings - packets_received) / num_pings) * 100
        print(f"{num_pings} pings and {packets_received} packets received\n")
        print(f"Summary: {min_rtt:.3f} :: {max_rtt:.3f} :: {avg_rtt:.3f} :: {packet_loss_rate:.2f}% packet loss")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERR - Incorrect number of arguments")
        sys.exit(1)
    
    hostname = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("ERR - Port must be a positive integer")
        sys.exit(1)
    
    ping_client(hostname, port)
