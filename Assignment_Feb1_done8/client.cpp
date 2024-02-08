#include <iostream>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <chrono>





int main()
{
    // Create a UDP socket
    int clientSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (clientSocket == -1){std::cerr << "Error creating socket\n";return -1;}

    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr("127.0.0.1"); // Server's IP     address
    serverAddress.sin_port = htons(8080); 


    // sockaddr_in clientAddress;
    // clientAddress.sin_family = AF_INET;
    // clientAddress.sin_addr.s_addr = INADDR_ANY; // Listen on any available interface
    // clientAddress.sin_port = htons(5000); 
    // Set up the server address



    auto begin = std::chrono::high_resolution_clock::now();
    // Server's port
    // Send data to the server
    const char *message = "Ping-from-client";

    for (int i = 0; i < 11; i++)
    {
        if(i==10){message="$$$$$$";}


        ssize_t bytesSent = sendto(clientSocket, message, strlen(message), 0,
                               (struct sockaddr *)&serverAddress,
                               sizeof(serverAddress));
    
        if (bytesSent == -1)
        {
            std::cerr << "Error sending data\n";
            close(clientSocket);
            return -1;
        }



        std::cout<<clientSocket<<"\n";
        if (clientSocket == -1)
        {
            std::cerr << "Error creating socket\n";
            return -1;
        }
    // sockaddr_in clientAddress;
    // clientAddress.sin_family = AF_INET;
    // clientAddress.sin_addr.s_addr = INADDR_ANY; // Listen on any available interface
    // clientAddress.sin_port = htons(4000);       // Use port 8080
    // if (bind(clientSocket, (struct sockaddr *)&clientAddress,
    //          sizeof(clientAddress)) == -1)
    // {

    //     std::cerr << "Error binding socket here\n";
    //     close(clientSocket);
    //     return -1;
    // }

    // Receive data from the client
        char buffer[1024];
    // sockaddr_in clientAddress;
        socklen_t serverAddrLen = sizeof(serverAddress);
        ssize_t bytesRead = recvfrom(clientSocket, buffer, sizeof(buffer), 0,

                                    (struct sockaddr *)&serverAddress,

                                    &serverAddrLen);
    // std::cout << "Received message from client: " << buffer << "\n";
        if (bytesRead == -1)
        {
            std::cerr << "Error receiving data\n";
            close(clientSocket);
            return -1;
        }
        // Display the received message
        
        std::cout << "Received message from Server: " << buffer << "\n";
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::cout <<"time taken is "<< std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count() << "ns" << std::endl;
    close(clientSocket);
    return 0;
}