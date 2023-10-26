import socket
import time

def lookup_stock(stock_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # Get local machine name
    # client_socket.connect((host, 8888))                               #hostname and port for connection
    client_socket.connect(("elnux1.cs.umass.edu", 8888))                #hostname and port for connection for edLab
    request = stock_name.encode("utf-8")                                #encoding the request to be sent to the server
    start_time = time.time()
    client_socket.sendall(request)
    msg = client_socket.recv(1024) 
    end_time = time.time()
    response = msg.decode("utf-8")
    latency = end_time - start_time
    return float(response) if response != "-1" else response, latency

if __name__ == "__main__":
    stock_names = ["GameStart", "FishCo", "Apple", "HelloWorld", "GameStart", "FishCo", "Apple", "HelloWorld","GameStart", "FishCo", "GameStart", "FishCo", "Apple", "HelloWorld", "GameStart", "FishCo", "Apple", "HelloWorld","GameStart", "FishCo"]
    total_latency = []

    for j in range(50):
        latency_per_run = 0
        for i in stock_names:
            ans, latency = lookup_stock(i)
            print(i," -> ",ans)
            latency_per_run += latency
        total_latency.append(latency_per_run)
    print("Total latency for all runs:", total_latency)
    print("Totalsum:", sum(total_latency))
