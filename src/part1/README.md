## Part 1: Implementation with Socket Connection and Handwritten Thread Pool

## How to Run

**Requires Python 3.6+**

First start the server:
```
python3 server.py
```

Then start the client in a separate terminal:
```
python3 client.py
```



## Connection changes to run the client

Hostname and Port name for connection for edLab in client.py (elnux1 - changes as per initialization)  [Current working in code]
```
client_socket.connect(("elnux1.cs.umass.edu", 8888))                
```

Hostname and Port name for connection locally
```
client_socket.connect((host, 8888))                               
```

Hostname and Port name for connection based on IP address for running client server on two seperate machines
```
client_socket.connect(("Insert your server machine's IP address here", 8888))                               
```