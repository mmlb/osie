# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hegel_pb2 as hegel__pb2


class HegelStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Get = channel.unary_unary(
            "/hegel.Hegel/Get",
            request_serializer=hegel__pb2.GetRequest.SerializeToString,
            response_deserializer=hegel__pb2.GetResponse.FromString,
        )
        self.Subscribe = channel.unary_stream(
            "/hegel.Hegel/Subscribe",
            request_serializer=hegel__pb2.SubscribeRequest.SerializeToString,
            response_deserializer=hegel__pb2.SubscribeResponse.FromString,
        )


class HegelServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Get(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Subscribe(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_HegelServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=hegel__pb2.GetRequest.FromString,
            response_serializer=hegel__pb2.GetResponse.SerializeToString,
        ),
        "Subscribe": grpc.unary_stream_rpc_method_handler(
            servicer.Subscribe,
            request_deserializer=hegel__pb2.SubscribeRequest.FromString,
            response_serializer=hegel__pb2.SubscribeResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "hegel.Hegel", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
