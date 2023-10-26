import grpc
import time
import random
import stockMarket_pb2
import stockMarket_pb2_grpc

# Defines server address and port number
#server_address = 'localhost:13579'
server_address = 'elnux1.cs.umass.edu' + ':13579'
print(server_address)

def run():
    # Creates an insecure channel to server
    channel = grpc.insecure_channel(server_address)
    stub = stockMarket_pb2_grpc.StockMarketStub(channel)

    # List of both valid and invalid stock names
    stockNames = ['GameStart', 'Google', 'FishCo', 'BoarCo', 'GE', 'MenhirCo', 'Amazon']
    # Generates a random number of trades a client will make
    # numOfTrades = random.randint(5, 50)
    numOfTrades = 1000
    total_lookup_latency = []
    total_trade_latency = []

    for i in range(numOfTrades):
        stockName = random.choice(stockNames)
        # Calls the lookup method is server
        lookup_start_time = time.time()
        lookupResponse = stub.LookUp(stockMarket_pb2.LookUpRequest(stockName=stockName))
        lookup_end_time = time.time()
        total_lookup_latency.append(lookup_end_time-lookup_start_time)
        if lookupResponse.stockPrice == -1:
            print(f'Invalid stock name: {stockName}')
        else:
            print(f'Current price for {stockName}: {lookupResponse.stockPrice}, volume: {lookupResponse.stockVol}')

        time.sleep(0.1)

        # Picks a random number of stocks to trade
        n = random.randint(1, 10)
        # Picks whether to buy or sell the stock
        tradeType = random.choice(['BUY', 'SELL'])
        # Calls the Trade method in server
        trade_start_time = time.time()
        tradeResponse = stub.Trade(stockMarket_pb2.TradeRequest(stockName=stockName, stockQuantity=n, stockType=tradeType))
        trade_end_time = time.time()
        total_trade_latency.append(trade_end_time-trade_start_time)
        if tradeResponse.tradeStatus == -1:
            print(f'Invalid stock name: {stockName}')
        elif tradeResponse.tradeStatus == 0:
            print(f'Trading is suspended for {stockName}')
        else:
            action = 'Bought' if tradeType == 'BUY' else 'Sold'
            print(f'{action} {n} shares of {stockName}')

        time.sleep(0.5)

    print(total_lookup_latency)
    print(total_trade_latency)
    print('Time taken for 1000 lookups: ', sum(total_lookup_latency))
    print('Time taken for 1000 trades: ', sum(total_trade_latency))

if __name__ == '__main__':
    run()
