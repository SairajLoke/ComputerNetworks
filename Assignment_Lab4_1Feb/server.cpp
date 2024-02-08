#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include<cstring>

int send_data(int Socket, sockaddr_in Address){
    const char* message = "Ponge\n";
    ssize_t bytesSent = sendto(Socket, message, strlen(message), 0,(struct sockaddr*)&Address,sizeof(Address));
    if (bytesSent == -1) {
        std::cerr << "Error sending data\n";
        close(Socket);
        return -1;
    }

    return bytesSent;
}


int create_server(){
    
    int serverSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (serverSocket == -1) {
        std::cerr << "Error creating socket\n";
        return -1;
    }
    return serverSocket;
}

int main() {
    
    // Create a UDP socket
    int serverSocket = create_server();

    // Bind the socket to an address and port
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY; // Listen on any available interface
    serverAddress.sin_port = htons(8080); // Use port 8080
    if (bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == -1) {
        std::cerr << "Error binding socket\n";
        close(serverSocket);
        return -1;
    }

    // Receive data from the client
    char buffer[1024];
    sockaddr_in clientAddress;
    socklen_t clientAddrLen = sizeof(clientAddress);
    ssize_t bytesRead = recvfrom(serverSocket, buffer, sizeof(buffer), 0,(struct sockaddr*)&clientAddress,&clientAddrLen);
    if (bytesRead == -1) {
        std::cerr << "Error receiving data\n";
        close(serverSocket);
        return -1;
    }

    // Display the received message
    std::cout << "Received message from client: " << buffer << "\n";
 

    sleep(2);
    std::cout<<"Bytes sent"<<send_data(serverSocket,clientAddress)<<std::endl;

    // Close socket
    close(serverSocket);
    return 0;
}