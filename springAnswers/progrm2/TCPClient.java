import java.io.*;
import java.net.*;

class TCPClient {

    public static void main(String argv[]) throws Exception
    {
	// TCP socket variables
	Socket clientSocket;
	DataOutputStream outToServer;
	BufferedReader inFromServer;
	
	// client variables
	BufferedReader inFromUser;
	String clientSentence, serverSentence;

	// command-line arguments
	String server;
	int port;

	// process command-line arguments
	if (argv.length < 2) {
	    System.out.println ("Usage: java TCPClient hostname port\n");
	    System.exit (-1);
	}
	server = argv[0];
	port = Integer.parseInt(argv[1]);

	// Create (buffered) input stream using standard input
        inFromUser = new BufferedReader(new InputStreamReader(System.in));  
      
	// Create client socket with connection to server at given port
	clientSocket = new Socket (server, port);
	
	// Create output stream attached to socket
	outToServer = new DataOutputStream(clientSocket.getOutputStream());

	// Create (buffered) input stream attached to socket
	inFromServer = new BufferedReader(new InputStreamReader(
					       clientSocket.getInputStream()));
	
	// Read line from user
        System.out.println("Client ready for input");
	clientSentence = inFromUser.readLine();

	// Write line to server (add newline)
	// Question: What happens if no newline added?  Why?
	outToServer.writeBytes(clientSentence + '\n');
	System.out.println ("TO SERVER: " + clientSentence);

	// Read line from server
	serverSentence = inFromServer.readLine();
	System.out.println("FROM SERVER: " + serverSentence);

	// Close the socket
	clientSocket.close();

    } // end main

} // end class
