# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stockMarket_pb2 as stockMarket__pb2


class StockMarketStub(object):
    """The stock market service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LookUp = channel.unary_unary(
                '/stockMarket.StockMarket/LookUp',
                request_serializer=stockMarket__pb2.LookUpRequest.SerializeToString,
                response_deserializer=stockMarket__pb2.LookUpResponse.FromString,
                )
        self.Trade = channel.unary_unary(
                '/stockMarket.StockMarket/Trade',
                request_serializer=stockMarket__pb2.TradeRequest.SerializeToString,
                response_deserializer=stockMarket__pb2.TradeResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/stockMarket.StockMarket/Update',
                request_serializer=stockMarket__pb2.UpdateRequest.SerializeToString,
                response_deserializer=stockMarket__pb2.UpdateResponse.FromString,
                )


class StockMarketServicer(object):
    """The stock market service definition.
    """

    def LookUp(self, request, context):
        """Sends the Price and Trading volume for the given Stock Name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Trade(self, request, context):
        """Sends 1 if the trade succeeds, 0 if trading is suspended, and -1 if an invalid stock name is specified in the detail
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Sends 1 if the update is successful, -1 if an invalid stock name is specified, and -2 if an invalid price (e.g, negative value) is specified
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockMarketServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LookUp': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUp,
                    request_deserializer=stockMarket__pb2.LookUpRequest.FromString,
                    response_serializer=stockMarket__pb2.LookUpResponse.SerializeToString,
            ),
            'Trade': grpc.unary_unary_rpc_method_handler(
                    servicer.Trade,
                    request_deserializer=stockMarket__pb2.TradeRequest.FromString,
                    response_serializer=stockMarket__pb2.TradeResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=stockMarket__pb2.UpdateRequest.FromString,
                    response_serializer=stockMarket__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stockMarket.StockMarket', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StockMarket(object):
    """The stock market service definition.
    """

    @staticmethod
    def LookUp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stockMarket.StockMarket/LookUp',
            stockMarket__pb2.LookUpRequest.SerializeToString,
            stockMarket__pb2.LookUpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Trade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stockMarket.StockMarket/Trade',
            stockMarket__pb2.TradeRequest.SerializeToString,
            stockMarket__pb2.TradeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stockMarket.StockMarket/Update',
            stockMarket__pb2.UpdateRequest.SerializeToString,
            stockMarket__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
