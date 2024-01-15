import grpc
import logging
from concurrent import futures
import mathematics_pb2, mathematics_pb2_grpc

class MathematicsServiceImplementation(mathematics_pb2_grpc.MathematicsServicer):
    def SumIntegers(self, request, context):
        return mathematics_pb2.ResponseInteger(result=request.num1 + request.num2)
    
    def SubIntegers(self, request, context):
        return mathematics_pb2.ResponseInteger(result=request.num1 - request.num2)
    
    def MultIntegers(self, request, context):
        return mathematics_pb2.ResponseInteger(result=request.num1 * request.num2)
    
    def DevIntegers(self, request, context):
        return mathematics_pb2.ResponseFloat(result=request.num1 / request.num2)
    

def serve():
    port = "243243"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mathematics_pb2_grpc.add_MathematicsServicer_to_server(MathematicsServiceImplementation(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print(f"Server listening on port {port}...")
    server.wait_for_termination()
    

if __name__ == '__main__':
    logging.basicConfig()
    serve()