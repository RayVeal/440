import java.io.*;
import java.net.*;

class UDPClient {

    public static void main(String argv[]) throws Exception
    {
	// socket variables
	DatagramSocket clientSocket;
	DatagramPacket sendPacket;
	DatagramPacket receivePacket;
	byte[] receiveData = new byte[1024];
	byte[] sendData = new byte[1024];
	InetAddress IPAddress;

	// client variables
	String clientSentence, serverSentence;
	BufferedReader inFromUser;

	// command-line arguments
	int port;
	String server;

	// process command-line arguments
	if (argv.length < 2) {
	    System.out.println ("Usage: java UDPServer hostname port\n");
	    System.exit (-1);
	}
	server = argv[0];
	port = Integer.parseInt(argv[1]);

	// Create (buffered) input stream using standard input
        inFromUser = new BufferedReader(new InputStreamReader(System.in));  
      
	// Create client socket to destination
	clientSocket = new DatagramSocket();
	IPAddress = InetAddress.getByName (server);

	// Get input from user
        System.out.println("Client ready for input");
	clientSentence = inFromUser.readLine();
	sendData = clientSentence.getBytes();

	// Create packet and send to server
	sendPacket = new DatagramPacket(sendData, sendData.length,  
					IPAddress, port);
	clientSocket.send(sendPacket);
	System.out.println ("TO SERVER: " + clientSentence);

	// Create receiving packet and receive from server
	receivePacket = new DatagramPacket(receiveData,
					   receiveData.length); 
	clientSocket.receive(receivePacket);
	serverSentence = new String(receivePacket.getData(), 0,
				    receivePacket.getLength());

	System.out.println("FROM SERVER: " + serverSentence);

	// close the socket
	clientSocket.close();

    } // end main

} // end class
