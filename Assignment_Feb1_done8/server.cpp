#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>


int main()
{
    // Create a UDP socket
    int serverSocket = socket(AF_INET, SOCK_DGRAM, 0);
    std::cout<<serverSocket<<"\n";
    if (serverSocket == -1)
    {
        std::cerr << "Error creating socket\n";
        return -1;
    }
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY; // Listen on any available interface
    serverAddress.sin_port = htons(8080);       // Use port 8080
    if (bind(serverSocket, (struct sockaddr *)&serverAddress,
             sizeof(serverAddress)) == -1)
    {

        std::cerr << "Error binding socket\n";
        close(serverSocket);
        return -1;
    }
    while (true)
    {
        // Receive data from the client
    char buffer[1024];
    sockaddr_in clientAddress;
    socklen_t clientAddrLen = sizeof(clientAddress);
    ssize_t bytesRead = recvfrom(serverSocket, buffer, sizeof(buffer), 0,

                                 (struct sockaddr *)&clientAddress,

                                 &clientAddrLen);
    // std::cout << "Received message from client: " << buffer << "\n";
    if (bytesRead == -1)
    {
        std::cerr << "Error receiving data\n";
        close(serverSocket);
        return -1;
    }
    // Display the received message
    
    std::cout << "Received message from client: " << buffer << "\n";



    
    const char *message = "Pong";
    ssize_t bytesSent = sendto(serverSocket, message, strlen(message), 0,

                               (struct sockaddr *)&clientAddress,

                               sizeof(serverAddress));
    if (bytesSent == -1)
    {
        std::cerr << "Error sending data\n";
        close(serverSocket);
        return -1;
    }
    if(buffer[0]=='$'){
        break;
    }
    }
    
    
    
    // Close socket
    close(serverSocket);
    return 0;
}