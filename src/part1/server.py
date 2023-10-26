import socket
import threading
import queue

lock = threading.Lock()

# defining the stocks along with their price and volume
stock_catalog = {
    "GameStart": {
        "price": 15.99,
        "volume": 2000
    },
    "FishCo": {
        "price": 10.99,
        "volume": 5000
    }
}

class ThreadPool:
    def __init__(self, num_threads):
        self.work_queue = queue.Queue()
        self.threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self):
        while True:
            try:
                #lock.aquire()
                request, client_socket = self.work_queue.get()
                #lock.release()
                response = handle_request(request)
                print(threading.current_thread().name, " ", response)
                client_socket.sendall(response)
            finally:
                client_socket.close()
                self.work_queue.task_done()

def handle_request(request):
    request = request.decode("utf-8")
    if request in stock_catalog:
        stock = stock_catalog[request]
        if stock["volume"] > 0:
            stock["volume"] -= 1                                            #stock volume is decreased by 1 on every lookup when it is found
            return str(stock["price"]).encode("utf-8")                      #stock is found and the price is returned
        else:
            return b"0"                                                     #stock is found but the volume remaining is 0
    else:
        return b"-1"                                                        #stock is not found

# start server
def start_server(port, num_threads):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # Get local machine name
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on port {port}...")

    thread_pool = ThreadPool(num_threads)

    while True:
        client_socket, address = server_socket.accept()     # Establish connection with client
        request = client_socket.recv(1024)
        #lock.aquire()
        thread_pool.work_queue.put((request, client_socket))
        # lock.release()

if __name__ == "__main__":
    start_server(8888, 3)