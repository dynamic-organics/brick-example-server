# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from brick_server.minimal.interfaces.actuation import (
    actuation_server_pb2 as actuation__server__pb2,
)


class ActuationServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ActuateSingleSensor = channel.unary_unary(
            "/actuationserver.ActuationServer/ActuateSingleSensor",
            request_serializer=actuation__server__pb2.SensorValue.SerializeToString,
            response_deserializer=actuation__server__pb2.Status.FromString,
        )
        self.ActuateMultiSensor = channel.stream_stream(
            "/actuationserver.ActuationServer/ActuateMultiSensor",
            request_serializer=actuation__server__pb2.SensorValue.SerializeToString,
            response_deserializer=actuation__server__pb2.Status.FromString,
        )


class ActuationServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ActuateSingleSensor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ActuateMultiSensor(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ActuationServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ActuateSingleSensor": grpc.unary_unary_rpc_method_handler(
            servicer.ActuateSingleSensor,
            request_deserializer=actuation__server__pb2.SensorValue.FromString,
            response_serializer=actuation__server__pb2.Status.SerializeToString,
        ),
        "ActuateMultiSensor": grpc.stream_stream_rpc_method_handler(
            servicer.ActuateMultiSensor,
            request_deserializer=actuation__server__pb2.SensorValue.FromString,
            response_serializer=actuation__server__pb2.Status.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "actuationserver.ActuationServer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ActuationServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ActuateSingleSensor(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/actuationserver.ActuationServer/ActuateSingleSensor",
            actuation__server__pb2.SensorValue.SerializeToString,
            actuation__server__pb2.Status.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ActuateMultiSensor(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/actuationserver.ActuationServer/ActuateMultiSensor",
            actuation__server__pb2.SensorValue.SerializeToString,
            actuation__server__pb2.Status.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
