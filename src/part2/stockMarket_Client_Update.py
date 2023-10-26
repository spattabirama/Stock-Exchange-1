import grpc
import time
import random
import stockMarket_pb2
import stockMarket_pb2_grpc

# server address and port number definition
server_address = 'localhost:13579'

def run():
    channel = grpc.insecure_channel(server_address)                                             # Creates a channel to server
    stub = stockMarket_pb2_grpc.StockMarketStub(channel)

    while True:
        
        stockName = random.choice(['GameStart', 'FishCo', 'BoarCo', 'MenhirCo', 'RanCo'])
        newPrice = round(random.uniform(-50, 500), 2)                                           # Including negative value to test invalid price

        # Calling Update method in server
        updateResponse = stub.Update(stockMarket_pb2.UpdateRequest(stockName=stockName, stockPrice=newPrice))
        if updateResponse.updateStatus == -1:
            print(f'Invalid stock name: {stockName}')
        elif updateResponse.updateStatus == -2:
            print(f'Invalid price for {stockName}: {newPrice}')
        else:
            print(f'{stockName} updated to {newPrice}')

        time.sleep(random.uniform(1, 10))


if __name__ == '__main__':
    run()
