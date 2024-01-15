import grpc
import logging
import mathematics_pb2, mathematics_pb2_grpc


def run():
    print("Calling the math functions from my gRPC server")
    num1 = 60
    num2 = 40
    with grpc.insecure_channel("localhost:243243") as channel:
        stub = mathematics_pb2_grpc.MathematicsStub(channel)
        response = stub.SumIntegers(mathematics_pb2.RequestIntegers(num1=num1, num2=num2))
        print(f"The sum of {num1} and {num2} is: {response.result}")
        response = stub.SubIntegers(mathematics_pb2.RequestIntegers(num1=num1, num2=num2))
        print(f"The diffrence between {num1} and {num2} is: {response.result}")
        response = stub.MultIntegers(mathematics_pb2.RequestIntegers(num1=num1, num2=num2))
        print(f"The product of {num1} and {num2} is: {response.result}")
        response = stub.DevIntegers(mathematics_pb2.RequestIntegers(num1=num1, num2=num2))
        print(f"The quotient of {num1} and {num2} is: {response.result}")


if __name__ == "__main__":
    logging.basicConfig()
    run()