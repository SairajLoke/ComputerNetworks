#!/bin/bash

echo "Client_Server.cpp"

g++ client.cpp -o client 
g++ server.cpp -o server

./server
