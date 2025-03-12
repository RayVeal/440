import java.io.*;
import java.net.*;

class UDPServer {

    public static void main(String argv[]) throws Exception
    {
	// socket variables
	DatagramSocket serverSocket;
	byte[] receiveData = new byte[1024];
	byte[] sendData = new byte[1024];
	InetAddress IPAddress;
	int clientPort;

	// server variables
	String serverSentence;

	// command-line arguments
	int port;

	// process command-line arguments
	if (argv.length < 1) {
	    System.out.println ("Usage: java UDPServer port\n");
	    System.exit (-1);
	}
	port = Integer.parseInt(argv[0]);

	// Create welcoming socket using given port
	serverSocket = new DatagramSocket(port);

	System.out.println("Listening on port " + port + "... ");

	// While loop to handle arbitrary sequence of clients making requests
	while (true) {

	    // Waits for some client to send a packet
	    DatagramPacket receivePacket = new DatagramPacket 
		(receiveData,receiveData.length);
	    serverSocket.receive(receivePacket);
	    // Question: What could happen if we didn't 
	    // only convert receivePacket.getLength() bytes?
    	    String clientSentence = new String(receivePacket.getData(), 0,
    					       receivePacket.getLength());
	    System.out.println("FROM CLIENT: " + clientSentence);

	    // Convert to all caps
	    serverSentence = clientSentence.toUpperCase();

	    // Write output line to socket
	    IPAddress = receivePacket.getAddress();
	    clientPort = receivePacket.getPort();
	    sendData = serverSentence.getBytes();
	    DatagramPacket sendPacket = new DatagramPacket(sendData, 
							   sendData.length, 
							   IPAddress, 
							   clientPort);
	    serverSocket.send(sendPacket);
	    System.out.println ("TO CLIENT: " + serverSentence);
	} //  end while; loop back to accept a new client connection

    } // end main

} // end class
