# Mathematics gRPC Service


## Overview

This repository contains the source code for a simple gRPC service that performs mathematical operations. The service is defined using Protocol Buffers and implements a basic API for addition.


## Features

Addition Operation: The gRPC service provides methods for adding, subtracting, multiplying, and dividing two numbers.


## Project Structure

- mathematics.proto: Protocol Buffers file defining the gRPC service and messages.
- server.py: Python script implementing the gRPC server.
- client.py: Python script implementing a gRPC client for testing.
- mathematics_pb2.py and mathematics_pb2_grpc.py: Auto-generated Python files from the mathematics.proto file.


## Requirements

- Python 3.x
- grpcio
- gRPC tools (grpcio-tools)


## Setup

1. Install dependencies:
```bash
    pip install -r requirements.txt
```

2. Generate gRPC code:
```bash
    python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. mathematics.proto
```


## Execution

1. Run the Server:
```bash
    python server.py
```
The server will start and listen on port 243243.

2. Run the Client:
```bash
    python client.py
```
he client sends sample requests to the server and prints the responses.