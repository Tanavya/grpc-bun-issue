from concurrent import futures
import os
import grpc
import time
import generated.helloworld.v1.service_pb2_grpc as hello_world_service_grpc
from generated.helloworld.v1.service_pb2 import HelloWorldRequest, HelloWorldResponse

class HelloWorldServiceServicer(hello_world_service_grpc.HelloWorldService):
    def HelloWorld(self, request: HelloWorldRequest, context):
        time.sleep(120)
        return HelloWorldResponse(result=f"Hello {request.name}!")

def main():
    port = os.environ.get("PORT")
    print(f"Starting server on port {port}")
    server = grpc.server(
        futures.ThreadPoolExecutor(
            max_workers=1,
        ),
    )
    hello_world_service_grpc.add_HelloWorldServiceServicer_to_server(HelloWorldServiceServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
