import grpc
import time
import hashlib
import digestor_pb2
import digestor_pb2_grpc
from concurrent import futures

class DigestorServicer(digestor_pb2_grpc.DigestorServicer):
    """
    gRPC server for Digestor Service
    """
    def __init__(self, *args, **kwargs):
        self.server_port = 46001

    def GetDigestor(self, request, context):
        """
        Implementation of the rpc GetDigest declared in the proto file
        """
        # get the string from the incoming request
        # defined in proto file (request = DigestMessage) as a argument for the service
        to_be_digested = request.ToDigest

        # do some work
        # digest and get the string representation from the digestor
        hasher = hashlib.sha256()
        hasher.update(to_be_digested.encode())
        digested = hasher.hexdigest()

        # print the output here
        print(digested)

        result = {'Digested': digested, 'WasDigested': True}

        # defined in the proto file as a return type, takes a dict as a set of arguments
        return digestor_pb2.DigestedMessage(**result)

    def start_server(self):
        """
        Function which actually starts the gRPC server, and preps
        it for serving incoming connections
        """
        # declare a server object with desired number
        # of thread pool workers.
        digestor_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # add digestor service
        digestor_pb2_grpc.add_DigestorServicer_to_server(DigestorServicer(),digestor_server)

        # bind the server to the port defined above
        digestor_server.add_insecure_port('[::]:{}'.format(self.server_port))

        # start the server
        digestor_server.start()
        print ('Digestor Server running ...')

        try:
            # need an infinite loop since the above
            # code is non blocking, and if I don't do this
            # the program will exit
            while True:
                time.sleep(60*60*60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print('Digestor Server Stopped ...')

curr_server = DigestorServicer()
curr_server.start_server()