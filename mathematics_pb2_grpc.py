# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mathematics_pb2 as mathematics__pb2


class MathematicsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SumIntegers = channel.unary_unary(
                '/mathematics.Mathematics/SumIntegers',
                request_serializer=mathematics__pb2.RequestIntegers.SerializeToString,
                response_deserializer=mathematics__pb2.ResponseInteger.FromString,
                )
        self.SubIntegers = channel.unary_unary(
                '/mathematics.Mathematics/SubIntegers',
                request_serializer=mathematics__pb2.RequestIntegers.SerializeToString,
                response_deserializer=mathematics__pb2.ResponseInteger.FromString,
                )
        self.MultIntegers = channel.unary_unary(
                '/mathematics.Mathematics/MultIntegers',
                request_serializer=mathematics__pb2.RequestIntegers.SerializeToString,
                response_deserializer=mathematics__pb2.ResponseInteger.FromString,
                )
        self.DevIntegers = channel.unary_unary(
                '/mathematics.Mathematics/DevIntegers',
                request_serializer=mathematics__pb2.RequestIntegers.SerializeToString,
                response_deserializer=mathematics__pb2.ResponseFloat.FromString,
                )


class MathematicsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SumIntegers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubIntegers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultIntegers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DevIntegers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathematicsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SumIntegers': grpc.unary_unary_rpc_method_handler(
                    servicer.SumIntegers,
                    request_deserializer=mathematics__pb2.RequestIntegers.FromString,
                    response_serializer=mathematics__pb2.ResponseInteger.SerializeToString,
            ),
            'SubIntegers': grpc.unary_unary_rpc_method_handler(
                    servicer.SubIntegers,
                    request_deserializer=mathematics__pb2.RequestIntegers.FromString,
                    response_serializer=mathematics__pb2.ResponseInteger.SerializeToString,
            ),
            'MultIntegers': grpc.unary_unary_rpc_method_handler(
                    servicer.MultIntegers,
                    request_deserializer=mathematics__pb2.RequestIntegers.FromString,
                    response_serializer=mathematics__pb2.ResponseInteger.SerializeToString,
            ),
            'DevIntegers': grpc.unary_unary_rpc_method_handler(
                    servicer.DevIntegers,
                    request_deserializer=mathematics__pb2.RequestIntegers.FromString,
                    response_serializer=mathematics__pb2.ResponseFloat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mathematics.Mathematics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mathematics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SumIntegers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mathematics.Mathematics/SumIntegers',
            mathematics__pb2.RequestIntegers.SerializeToString,
            mathematics__pb2.ResponseInteger.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubIntegers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mathematics.Mathematics/SubIntegers',
            mathematics__pb2.RequestIntegers.SerializeToString,
            mathematics__pb2.ResponseInteger.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultIntegers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mathematics.Mathematics/MultIntegers',
            mathematics__pb2.RequestIntegers.SerializeToString,
            mathematics__pb2.ResponseInteger.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DevIntegers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mathematics.Mathematics/DevIntegers',
            mathematics__pb2.RequestIntegers.SerializeToString,
            mathematics__pb2.ResponseFloat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
