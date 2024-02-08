#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include<cstring>


int create_socket(){
    int clientSocket = socket(AF_INET, SOCK_DGRAM, 0);
                        /*   AF_INET: 
                            SOCK_DGRAM: 
                            0 :
                        */

    if (clientSocket == -1) {
        std::cerr << "Error creating socket\n";
        return -1;
    }

    return clientSocket;
}

int send_data(int clientSocket, sockaddr_in serverAddress){
    const char* message = "Hello UDP Server";
    ssize_t bytesSent = sendto(clientSocket, message, strlen(message), 0,(struct sockaddr*)&serverAddress,sizeof(serverAddress));
    if (bytesSent == -1) {
        std::cerr << "Error sending data\n";
        close(clientSocket);
        return -1;
    }

    return bytesSent;
}

int main() {
    // Create a UDP socket
    int clientSocket = create_socket();

    // Set up the server address
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr("127.0.0.1"); // Server's IP address
    serverAddress.sin_port = htons(8080); // Server's port
    
    // Send data to the server
    std::cout<<"Bytes sent"<<send_data(clientSocket,serverAddress)<<std::endl;


    // //recv data from server
    // char buffer[1024];
    // // sockaddr_in serverAddress;
    // socklen_t serverAddrLen = sizeof(serverAddress);
    // ssize_t bytesRead = recvfrom(clientSocket, buffer, sizeof(buffer), 0,(struct sockaddr*)&serverAddress,&serverAddrLen);


    // Close socket
    close(clientSocket);
    return 0;
}