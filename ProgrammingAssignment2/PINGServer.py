""" Ramon Veal
cmsc 440
fall 2023 
programming assignment 2"""

import socket
import sys
import signal

def pack_packet(seq_no, timestamp, size, hostname, version=1):
    payload = f"Host: {hostname.upper()}\nClass-name: VCU-CMSC440-FALL-2023\nUser-name: Veal, Ramon"
    
    header = f"----------- Ping Reply Header -----------\nVersion: {version}\nSequence No.: {seq_no}\nTime: {timestamp}\nPayload Size: {size}\n"
    payload_section = "----------- Ping Reply Payload -----------\n" + payload + "\n------------------------------------------"
    
    return header + payload_section

# for ending code with ctrl c
""" def handler(signum, frame):
    Catch <ctrl+c> signal for clean stop
    print('\nNice exit')
    sys.exit(0)
    
signal.signal(signal.SIGINT, handler) """

def ping_server(port):
    # Create UDP socket
    server_address = ('localhost', port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        sock.bind(server_address)
        print(f"Server ready to receive on port {port}")
        
        while True:
             # Receive message from client along with its addres
            data, addr = sock.recvfrom(1024)
            client_ip, client_port = addr
            
            seq_no, timestamp, size, payload = parse_packet(data.decode())
            print(f"{client_ip} :: {client_port} :: {seq_no} :: RECEIVED\n")
            
            # Send the received message back to the client without any modification
            reply_packet = pack_packet(seq_no, timestamp, size, payload)
            print(reply_packet)
            sock.sendto(reply_packet.encode(), addr)
            
    
    except Exception as e:
        print(f"ERR - {str(e)}")
    
    finally:        
        sock.close()
    
# Parse response packet
def parse_packet(packet):
    lines = packet.split('\n')
    seq_no = int(lines[2].split(": ")[1])
    timestamp = float(lines[3].split(": ")[1])
    size = int(lines[4].split(": ")[1])
    payload = '\n'.join(lines[7:])
    
    return seq_no, timestamp, size, payload

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: PINGServer.py <port>")
        sys.exit(1)
    
    try:
        port = int(sys.argv[1])
        if not (0 < port < 65536):
            raise ValueError("Port must be a positive integer less than 65536")
    except ValueError as e:
        print(f"ERR - {str(e)}")
        sys.exit(1)
    
    ping_server(port)
