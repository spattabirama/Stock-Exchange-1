## Part 2: Implementation with gRPC and Built in Thread Pool

**Requires Python 3.6+**

## Quick Start

Install dependencies:

```
pip3 install grpcio grpcio-tools
```

## How to Run

First start the server:
```
python3 stockMarket_Server.py
```

Then start the client in a separate terminal: (for lookup and trade)
```
python3 stockMarket_Client_LookUpAndTrade.py
```

Then start the client update file in a separate terminal: (for updating the price of particular stock)
```
python3 stockMarket_Client_Update.py
```



## Connection changes to run the client

Hostname and Port name for connection for edLab in client.py (elnux1 - changes as per initialization)  [Current working in code]
```
server_address = 'elnux1.cs.umass.edu' + ':13579'
```

Hostname and Port name for connection locally
```
server_address = 'localhost' + ':13579'
```

Hostname and Port name for connection based on IP address for running client server on two seperate machines
```
server_address = 'Insert your server machine's IP address here' + ':13579'
```