from concurrent import futures
import threading
import grpc
import stockMarket_pb2
import stockMarket_pb2_grpc
import logging

# Creates lock for synchronization
catalogLock = threading.Lock()


# Defines Service for Stock Market Lookup, Trading and Update
class StockMarketService(stockMarket_pb2_grpc.StockMarketServicer):
    def __init__(self):
        # Defines stock catalog
        self.catalog = {
            'GameStart': {'price': 150, 'volume': 56},
            'FishCo': {'price': 50, 'volume': 78},
            'BoarCo': {'price': 200, 'volume': 93},
            'MenhirCo': {'price': 150, 'volume': 34}
        }
        # Maximum number of stocks per company
        self.maxVolume = 100

    # LookUp method returns the price and trading volume for the requested stock name
    def LookUp(self, request, context):
        with catalogLock:
            # Returns -1 if stock name is not in the catalog
            if request.stockName not in self.catalog:
                return stockMarket_pb2.LookUpResponse(stockPrice=-1, stockVol=0)
            # Returns the current price of the given stock name
            else:
                return stockMarket_pb2.LookUpResponse(stockPrice=self.catalog[request.stockName]['price'], stockVol=self.catalog[request.stockName]['volume'])

    # Trade method executes stock trade and returns the status of the trade
    def Trade(self, request, context):
        with catalogLock:
            # Returns -1 if stock name is not in the catalog
            if request.stockName not in self.catalog:
                return stockMarket_pb2.TradeResponse(tradeStatus=-1)
            else:
                if request.stockType == 'BUY':
                    # Returns 0 if the total volume after purchase crosses maximum trading volume
                    if self.catalog[request.stockName]['volume'] - request.stockQuantity < 0:
                        return stockMarket_pb2.TradeResponse(tradeStatus=0)
                    # Returns 1 after updating the trading volume
                    else:
                        self.catalog[request.stockName]['volume'] -= request.stockQuantity
                        return stockMarket_pb2.TradeResponse(tradeStatus=1)
                elif request.stockType == 'SELL':
                    # Returns 0 if the calculated total volume of after sale goes below zero
                    if self.catalog[request.stockName]['volume'] + request.stockQuantity > self.maxVolume:
                        return stockMarket_pb2.TradeResponse(tradeStatus=0)
                    # Returns 1 after updating the trading volume
                    else:
                        self.catalog[request.stockName]['volume'] += request.stockQuantity
                        return stockMarket_pb2.TradeResponse(tradeStatus=1)

    # Update method sets price for each company's stocks and returns the status of the update
    def Update(self, request, context):
        with catalogLock:
            # Returns -1 if stock name is not in the catalog
            if request.stockName not in self.catalog:
                return stockMarket_pb2.UpdateResponse(updateStatus=-1)
            # Returns -2 if stock price is invalid
            elif request.stockPrice < 0:
                return stockMarket_pb2.UpdateResponse(updateStatus=-2)
            # Returns 1 after updating stock price
            else:
                self.catalog[request.stockName]['price'] = request.stockPrice
                return stockMarket_pb2.UpdateResponse(updateStatus=1)


def serve():
    port = '13579'
    # Creates a gRPC server instance with a ThreadPool
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3), maximum_concurrent_rpcs=30)
    # Registers a service with the server
    stockMarket_pb2_grpc.add_StockMarketServicer_to_server(StockMarketService(), server)
    # Binds the server to the defined port
    server.add_insecure_port('[::]:' + port)
    # Starts the server
    server.start()
    print("Server has started. Listening on port: %s!" % port)
    # Run the server until interrupted by Keyboard
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
